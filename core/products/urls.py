from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductVariationListView.as_view(), name='product-variation-home'),
    path('create/', views.ProductVariationCreateView.as_view(), name="product-variation-create"),
    path('<int:pk>/', views.ProductVariationDetailView.as_view(), name="product-variation-detail"),
    path('<int:pk>/edit/', views.ProductVariationEditView.as_view(), name="product-variation-edit"),
    path('<int:pk>/delete/', views.ProductVariationDeleteView.as_view(), name="product-variation-delete"),
    
]
