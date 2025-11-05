from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginForm(AuthenticationForm):
    
    email = forms.CharField(widget=forms.EmailInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password"]


class RegisterForm(UserCreationForm):
    
    email = forms.CharField(widget=forms.EmailInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="confirm password")
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]