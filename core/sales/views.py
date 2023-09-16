from audioop import reverse
from django.shortcuts import redirect, render
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Sale, SaleDetail
from .forms import SaleForm, SaleDetailFormSet, SaleFormSet
from .mixins import AdminRequiredMixin


class SalesListView(AdminRequiredMixin, ListView):
    model = Sale
    template_name = 'sales/home.html'
    ordering = ['-id', '-date']
    paginate_by = 5


class SaleCreateView(AdminRequiredMixin, CreateView):
    model = Sale
    template_name = 'sales/sale_form.html'
    form_class = SaleForm
    success_url = reverse_lazy('sales-home')  # Replace with your success URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = SaleDetailFormSet(self.request.POST, prefix='sale_detail')
        else:
            # Pass an empty formset when not POST
            context['formset'] = SaleDetailFormSet(prefix='sale_detail', queryset=SaleDetail.objects.none())
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        # Process the SaleDetail formset
        if formset.is_valid():
            sale = form.save()
            
            for sale_detail_form in formset:
                if sale_detail_form.cleaned_data.get('product_variation'):
                    print('hermit4')
                    Sale_detail = sale_detail_form.save(commit=False)
                    Sale_detail.sale = sale
                    Sale_detail.save()

        else:
            # If formset is not valid, you can access formset.errors
            print(formset.errors)                    
            return render(
                self.request,
                self.template_name,
                context={'form': form, 'formset': formset},
            )            

        return super().form_valid(form)


class SaleDetailView(AdminRequiredMixin, DetailView):
    model = Sale

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        sale = self.object
        sale_details = sale.sale_detail.all()
        
        context['sale_details'] = sale_details
        return context


class SaleEditView(AdminRequiredMixin, UpdateView):
    model = Sale
    template_name = 'sales/sale_form.html'
    form_class = SaleForm
    success_url = reverse_lazy('sales-home')  # Replace with your success URL
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve the existing Sale instance
        sale = self.object

        if self.request.POST:
            formset = SaleFormSet(self.request.POST, prefix='sale_detail', queryset=SaleDetail.objects.filter(sale=sale))
        else:
            formset = SaleFormSet(instance=sale, queryset=SaleDetail.objects.filter(sale=sale))

        context['formset'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        # Process the SaleDetail formset
        if formset.is_valid():
            # Update the Sale instance
            sale = form.save()

            # First, Delete existing SaleDetail instances related to this Sale
            SaleDetail.objects.filter(sale=sale).delete()

            # Second, save all the SaleDetail again
            # Create new SaleDetail instances
            sale_details = []
            for sale_detail_form in formset:
                if sale_detail_form.cleaned_data.get('product_variation'):
                    sale_detail = sale_detail_form.save(commit=False)
                    sale_detail.sale = sale
                    # sale_detail.save()
                    sale_details.append(sale_detail)
            
            # Bulk insert the new SaleDetail instances
            SaleDetail.objects.bulk_create(sale_details)

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


class SaleDeleteView(AdminRequiredMixin, DeleteView):
    model = Sale
    success_url = reverse_lazy('sales-home')
    