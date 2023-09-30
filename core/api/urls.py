from django.urls import path
from .views import PurchaseListCreateView, PurchaseRetrieveUpdateDestroyView, SaleListCreateView, SaleRetrieveUpdateDestroyView, ProductVariationListCreateView, ProductVariationRetrieveUpdateDestroyView

# from rest_framework.authtoken import views

from .custom_auth_views import CustomAuthToken


urlpatterns = [
    path('purchases/', PurchaseListCreateView.as_view()),
    path('purchases/<int:pk>/', PurchaseRetrieveUpdateDestroyView.as_view()),

    path('sales/', SaleListCreateView.as_view()),
    path('sales/<int:pk>/', SaleRetrieveUpdateDestroyView.as_view()),

    path('products/', ProductVariationListCreateView.as_view()),
    path('products/<int:pk>/', ProductVariationRetrieveUpdateDestroyView.as_view()),

    # path('api-token-auth/', views.obtain_auth_token),
    # I was using this default before CustomAuthToken that make sure only super user can login in the api and auto generate token

    path('api-token-auth/', CustomAuthToken.as_view()),
]