from django.shortcuts import render
from django.views.generic import ListView
from products.models import ProductVariation


def home(request):
    return render(request, 'pages/home.html')


class HomeListView(ListView):
    model = ProductVariation
    template_name = 'pages/home.html'
    # context_object_name = 'products'

    def get_queryset(self):
        # Get the queryset of ProductVariation objects
        queryset = super().get_queryset()
        # Use slicing to limit the queryset to the first 3 objects
        queryset = queryset[:3]

        # Iterate through each object and calculate current inventory quantity
        for variation in queryset:
            variation.current_quantity = variation.current_inventory_quantity()

        return queryset



def about(request):
    return render(request, 'pages/about.html')

