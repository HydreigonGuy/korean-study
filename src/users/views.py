from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def user_login(request):
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