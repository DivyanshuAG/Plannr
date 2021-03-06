from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def register(response): 
    form = RegisterForm()
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            messages.info(response, f"Account successfully created, please sign in.")
            return redirect("loginView")
        else:
            messages.error(response,"Your information was invalid, please try again")
            return render(response, "registration/register.html", {"form": form})
    return render(response, "registration/register.html", {"form": form})


def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None: 
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("main")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")

    form = AuthenticationForm()
    return render(request, "registration/login.html/", {"form": form})

def logoutView(response):
    if response.method == "GET":
        logout(response)
        messages.success(response,"You have been successfully logged out")
        return redirect('loginView')
    return redirect(response, 'loginView')

