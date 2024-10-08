from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm

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
        try:
            if form.is_valid():
                user = form.save()
                login(request,user)
                return redirect('/')
            else:
                messages.success(request, ("Registration failed."))
                redirect('/user/user_register')
        except:
            messages.success(request, ("Reg failed."))
            redirect('/user/user_register')

    else:
        form = RegistrationForm()
        return render(request, 'register.html', {'form':form})
