from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, RegisterForm

def log_in(request):
    
    form = LoginForm()
    
    if request.POST:
        
        form = LoginForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            
            user = authenticate(request, username=username, email=email, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("main:home")
            else:
                messages.error(request, "Invalid password.")
    
    data = {
        'form': form,
    }
    
    return render(request, "authentication/login.html", context=data)


def sign_up(request):
    
    form = RegisterForm()
    
    if request.method == "POST":
        
        form = RegisterForm(request.POST)
       
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect("auth:login")
            
    data = {
        'form': form,
    }
    
    return render(request, "authentication/register.html", context=data)


def log_out(request):
    
    logout(request)
    
    return redirect("auth:login")