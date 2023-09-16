from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from posts.models import Post
from .mixins import AdminRequiredMixin


def home(request):
    return render(request, 'posts/home.html')


def about(request):
    return render(request, 'posts/about.html')


class PostListView(ListView):
    model = Post
    # this is the default convention if you don't set the template_name
    # <app>/<model>_<viewtype>.html
    template_name = 'posts/home.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 5


class PostCreateView(AdminRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    # default convention if you don't set the template_name
    # <app>/<model>_<viewtype>.html
    # https://youtu.be/-s7e_Fy6NRU?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&t=1304
    # explain why the default is not post_create.html but post_form.html
    # post_form.html

    def form_valid(self, form):
        # get the current login user and set that to the author of this post
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostDetailView(DetailView):
    model = Post
    # this is the default convention if you don't set the template_name
    # <app>/<model>_<viewtype>.html    
    # post_detail.html


# LoginRequiredMixin so that only login user can access this
# UserPassesTestMixin so that the owner of the post can only update its own post
# class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
class PostEditView(AdminRequiredMixin, UserPassesTestMixin, UpdateView):    
    model = Post
    fields = ['title', 'content']
    # post_form.html by default

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    # so that the owner of the post can only update its own post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True

        return False


# class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
class PostDeleteView(AdminRequiredMixin, UserPassesTestMixin, DeleteView):    
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True

        return False
    