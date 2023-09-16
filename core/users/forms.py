from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from users.models import CustomUser


class CustomUserRegistrationForm(UserCreationForm):
    # idk the use of the next line below. We already use meta for this
    # note that he's also using plane old inputs in the html rather than looping the fields
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2')


class CustomUserAuthenticationForm(forms.ModelForm):
    # idk the use of the next line below. We already use meta for this
    # note that he's also using plane old inputs in the html rather than looping the fields
    password = forms.CharField(label='Enter your password', widget=forms.PasswordInput)
    # the widget=forms.PasswordInput characters entered by the user are masked with asterisks (or bullets)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid login")


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username')

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                customuser = CustomUser.objects.exclude(pk=self.instance.pk).get(email=email)
            except CustomUser.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % email)

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                customuser = CustomUser.objects.exclude(pk=self.instance.pk).get(username=username)
            except CustomUser.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" is already in use.' % username)
