from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, authenticate, login
from authentication.forms import RegisterForm
from main.models import Note


@login_required(login_url="auth:login")
def statistics(request):
    
    note_count = Note.objects.filter(author=request.user).count()
    
    data = {
        'note_count': note_count
    }
    
    return render(request, "studio/studio.html" , context=data)


@login_required(login_url="auth:login")
def edit_account(request, username):
    
    user_form = RegisterForm(instance=request.user)
    
    if request.method == "POST":
        
        edit = request.POST.get("user-edit")
        
        if edit:
            try:
                user_edit_form = RegisterForm(request.POST, instance=request.user)
                if user_edit_form.is_valid:
                    user = user_edit_form.save()
                    update_session_auth_hash(request, user)
                    return redirect("studio:statistics")
            except Exception:
                print("Smth went wrong.")
        
        delete = request.POST.get("user-delete")
        
        if delete:
            try:
                User.objects.get(pk=request.user.pk, username=username).delete()
                print("deleted")
                return redirect("main:home")
            except Exception:
                print("Smth went wrong")
    
    
    data = {
        'user_form': user_form
    }
    
    return render(request, 'studio/account.html', context=data)