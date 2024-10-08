from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm

from models.models import Profile

def user_login(request):
    if request.user.is_authenticated:
            return redirect("/")

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.success(request, ("Login failed."))
            return redirect("/user/user_login")

    else:
        return render(request, 'login.html', {})

def user_logout(request):
    logout(request)
    return redirect("/user/user_login")

def user_register(request):
    if request.user.is_authenticated:
            return redirect("/")

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            newProfile = Profile(user=user)
            newProfile.save()
            messages.success(request, ("Account created."))
            return redirect('/user/user_login')
        else:
            return render(request, 'register.html', {'form':form})
    
    else:
        form = RegistrationForm()
        return render(request, 'register.html', {'form':form})
