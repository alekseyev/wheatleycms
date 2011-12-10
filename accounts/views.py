from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save()
        return redirect("/")
    return render(request, "registration/register.html", {'form': form})