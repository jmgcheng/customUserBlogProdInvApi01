from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from files.models import File
from users.models import CustomUser
from .mixins import AdminRequiredMixin


class FileCreateView(AdminRequiredMixin, CreateView):
    model = File
    fields = ['file']
    success_url = '/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class FileListView(AdminRequiredMixin, ListView):
    model = File
    template_name = 'files/home.html'
    context_object_name = 'files'
    ordering = ['-date']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["media_url"] = settings.MEDIA_URL
        return context    
    
    def get_queryset(self):
        user = get_object_or_404(CustomUser, email=self.request.user.email)
        return File.objects.filter(owner=user).order_by('-date')    
    