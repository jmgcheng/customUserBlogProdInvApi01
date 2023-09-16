from audioop import reverse
from django.shortcuts import redirect, render
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Purchase, PurchaseDetail
from .forms import PurchaseForm, PurchaseDetailFormSet, PurchaseFormSet
from .mixins import AdminRequiredMixin


class PurchasesListView(AdminRequiredMixin, ListView):
    model = Purchase
    template_name = 'purchases/home.html'
    ordering = ['-id', '-date']
    paginate_by = 5


class PurchaseCreateView(AdminRequiredMixin, CreateView):
    model = Purchase
    template_name = 'purchases/purchase_form.html'
    form_class = PurchaseForm
    success_url = reverse_lazy('purchases-home')  # Replace with your success URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PurchaseDetailFormSet(self.request.POST, prefix='purchase_detail')

            print('hermit1')
            print(self.request.POST)
            print('hermit1')

        else:
            # Pass an empty formset when not POST
            context['formset'] = PurchaseDetailFormSet(prefix='purchase_detail', queryset=PurchaseDetail.objects.none())
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        # Process the PurchaseDetail formset
        if formset.is_valid():
            purchase = form.save()

            for purchase_detail_form in formset:
                if purchase_detail_form.cleaned_data.get('product_variation'):
                    purchase_detail = purchase_detail_form.save(commit=False)
                    purchase_detail.purchase = purchase
                    purchase_detail.save()

        else:
            # If formset is not valid, you can access formset.errors
            print(formset.errors)                    
            return render(
                self.request,
                self.template_name,
                context={'form': form, 'formset': formset},
            )            

        return super().form_valid(form)


class PurchaseDetailView(AdminRequiredMixin, DetailView):
    model = Purchase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        purchase = self.object
        purchase_details = purchase.purchase_detail.all()
        
        context['purchase_details'] = purchase_details
        return context


class PurchaseEditView(AdminRequiredMixin, UpdateView):
    model = Purchase
    template_name = 'purchases/purchase_form.html'
    form_class = PurchaseForm
    success_url = reverse_lazy('purchases-home')  # Replace with your success URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve the existing Purchase instance
        purchase = self.object

        if self.request.POST:
            formset = PurchaseFormSet(self.request.POST, prefix='purchase_detail', queryset=PurchaseDetail.objects.filter(purchase=purchase))
        else:
            formset = PurchaseFormSet(instance=purchase, queryset=PurchaseDetail.objects.filter(purchase=purchase))

        context['formset'] = formset
        return context


    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        # Process the PurchaseDetail formset
        if formset.is_valid():

            # Update the Purchase instance
            purchase = form.save()

            # First, Delete existing PurchaseDetail instances related to this Purchase
            PurchaseDetail.objects.filter(purchase=purchase).delete()

            # Second, save all the PurchaseDetail again
            # Create new PurchaseDetail instances
            purchase_details = []
            for purchase_detail_form in formset:
                if purchase_detail_form.cleaned_data.get('product_variation'):
                    purchase_detail = purchase_detail_form.save(commit=False)
                    purchase_detail.purchase = purchase
                    # purchase_detail.save()
                    purchase_details.append(purchase_detail)
            
            # Bulk insert the new PurchaseDetail instances
            PurchaseDetail.objects.bulk_create(purchase_details)

        else:
            # If formset is not valid, you can access formset.errors
            print(formset.errors)
            print(formset.non_form_errors())
            return render(
                self.request,
                self.template_name,
                context={'form': form, 'formset': formset},
            )               

        return super().form_valid(form)


class PurchaseDeleteView(AdminRequiredMixin, DeleteView):
    model = Purchase
    success_url = reverse_lazy('purchases-home')
    