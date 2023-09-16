from django.urls import path
from . import views


"""
suggested crud url structure
angular reactive forms - Introduction - Demo Form and Sample Application - 06:23
products - list of products
products/1 - product detail of 1
products/1/edit - edit product detail of 1
products/0/edit - add new product. But this will be an issue in <slug>. Chatgpt note
"""
urlpatterns = [
    # path('', views.home, name='post-home'),
    # path('about/', views.about, name='post-about'),
    
    # path('post/create/', views.PostCreateView.as_view(), name="post-create"),
    # path('post/<slug>/', views.PostDetailView.as_view(), name="post-detail"),
    # path('post/<int:pk>/edit/', views.PostEditView.as_view(), name="post-edit"),
    # path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name="post-delete"),

    path('', views.PostListView.as_view(), name='post-home'),
    path('create/', views.PostCreateView.as_view(), name="post-create"),
    path('<slug>/', views.PostDetailView.as_view(), name="post-detail"),
    path('<int:pk>/edit/', views.PostEditView.as_view(), name="post-edit"),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name="post-delete"),
    
    
]
