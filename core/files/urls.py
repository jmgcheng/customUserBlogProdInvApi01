from django.urls import path
from . import views


urlpatterns = [
    path('', views.FileListView.as_view(), name='file-home'),
    path('upload/', views.FileCreateView.as_view(), name="file-upload"),
        
]
