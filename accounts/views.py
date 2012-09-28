from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User

from .forms import AccountCreationForm

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        if username.find('@') > 0:
            try: 
                username = User.objects.get(email=username).username
            except User.DoesNotExist:
                return render(request, 'registration/login.html', {'incorrect_login': True})    
        user = authenticate(
            username=username, 
            password=request.POST['password']
        )
        if user is not None and user.is_active:
            auth_login(request, user)
            if request.POST['next']:
                return redirect(request.POST['next'])
            else:
                return redirect('/')
        else:
            return render(request, 'registration/login.html', {'incorrect_login': True})
    else:
        return render(request, 'registration/login.html')

def register(request):
    form = AccountCreationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save()
        return redirect("/")
    return render(request, "registration/register.html", {'form': form})