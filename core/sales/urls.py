from django.urls import path
from . import views


urlpatterns = [
    path('', views.SalesListView.as_view(), name="sales-home"),
    path('create/', views.SaleCreateView.as_view(), name="sales-create"),
    path('<int:pk>/', views.SaleDetailView.as_view(), name="sales-detail"),
    path('<int:pk>/edit/', views.SaleEditView.as_view(), name="sales-edit"),
    path('<int:pk>/delete/', views.SaleDeleteView.as_view(), name="sales-delete"),
]
