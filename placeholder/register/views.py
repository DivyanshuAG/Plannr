from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login


def register(response): 
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return render(response, "registration/register.html", {"form": form})
    else:
        form = RegisterForm()

    return render(response, "registration/register.html", {"form": form})


def login(request): 
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None: 
        login(request, user)
        return redirect("/registration/loginSuccess")
    else:
        return "You failed to login successfully"


def loginSuccess(response):
    return redirect("main")
    