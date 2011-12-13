from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

def login(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'], 
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
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save()
        return redirect("/")
    return render(request, "registration/register.html", {'form': form})