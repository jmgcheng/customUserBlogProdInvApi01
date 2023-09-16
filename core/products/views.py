from django.shortcuts import redirect, render
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, ProductVariation
from .forms import ProductVariationCommentForm
from .mixins import AdminRequiredMixin


class ProductVariationListView(ListView):
    model = ProductVariation
    template_name = 'products/home.html'
    # context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        # Get the queryset of ProductVariation objects
        queryset = super().get_queryset()

        # Iterate through each object and calculate current inventory quantity
        for variation in queryset:
            variation.current_quantity = variation.current_inventory_quantity()

        return queryset    


class ProductVariationDetailView(DetailView):
    model = ProductVariation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_variation = self.get_object()
        current_quantity = product_variation.current_inventory_quantity()
        context['current_quantity'] = current_quantity
        context['product_variation_comment_form'] = ProductVariationCommentForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ProductVariationCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product_variation = self.get_object()  # Set the related product_variation
            comment.user = request.user  # Set the user
            comment.save()
        return redirect(self.request.path_info)  # Redirect back to the same page    


class ProductVariationCreateView(AdminRequiredMixin, CreateView):
    model = ProductVariation
    fields = ['code', 'product', 'name', 'image_url', 'excerpt', 'description', 'unit', 'size', 'color']


class ProductCreateView(AdminRequiredMixin, CreateView):
    model = Product
    fields = ['code', 'name', 'image_url', 'excerpt', 'description']


class ProductVariationEditView(AdminRequiredMixin, UpdateView):
    model = ProductVariation
    fields = ['code', 'product', 'name', 'image_url', 'excerpt', 'description', 'unit', 'size', 'color']


class ProductVariationDeleteView(AdminRequiredMixin, DeleteView):
    model = ProductVariation

    def get_success_url(self):
        return reverse("product-variation-home")
    