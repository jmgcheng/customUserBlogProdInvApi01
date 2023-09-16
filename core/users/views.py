from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from users.forms import CustomUserRegistrationForm, CustomUserAuthenticationForm, CustomUserUpdateForm


def registration_view(request):
    context = {}
    if request.POST:
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            messages.success(request, f'Your account has been created!')
            return redirect('post-home')
        else:
            context['form'] = form
    else:
        form = CustomUserRegistrationForm()
        context['form'] = form
    return render(request, 'users/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("post-home")

    if request.POST:
        form = CustomUserAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("post-home")
    else:
        form = CustomUserAuthenticationForm()

    context['form'] = form
    return render(request, 'users/login.html', context)


# decorator to enforce only login users can go to this page
@login_required
def profile_view(request):
    context = {}
    if request.POST:
        form = CustomUserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        form = CustomUserUpdateForm(instance=request.user)

    context['form'] = form

    # blog_posts = BlogPost.objects.filter(author=request.user)
    # context['blog_posts'] = blog_posts

    return render(request, "users/profile.html", context)
