from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class LoginForm(forms.Form):
    
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter your username"}), label="Login")
    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder":"Email address"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Enter your password"}))

    class Meta:
        fields = ["username", "password", "email"]


class RegisterForm(UserCreationForm):
    
    email = forms.CharField(widget=forms.EmailInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="confirm password")
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    
    def clean(self) -> dict[str, Any]:
        
        cleaned_data = super().clean()

        if cleaned_data.get("password1") != cleaned_data.get("password2"):
            raise ValidationError("Passwords does not match!")
        
        return cleaned_data
    

class UpdateAccountForm(UserChangeForm):
    
    email = forms.CharField(widget=forms.EmailInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password"]