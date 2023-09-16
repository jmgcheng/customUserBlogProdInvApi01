from django.urls import path
from . import views


urlpatterns = [
    path('', views.PurchasesListView.as_view(), name="purchases-home"),
    path('create/', views.PurchaseCreateView.as_view(), name="purchases-create"),
    path('<int:pk>/', views.PurchaseDetailView.as_view(), name="purchases-detail"),
    path('<int:pk>/edit/', views.PurchaseEditView.as_view(), name="purchases-edit"),
    path('<int:pk>/delete/', views.PurchaseDeleteView.as_view(), name="purchases-delete"),
]
