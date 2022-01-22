from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def register(response): 
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response, "Your account has been created!")
            return render(response, "registration/login.html", {"form": form})
        else:
            messages.error(response, "Invalid form entry, please try again.")
            form = RegisterForm()
    else:
        form = RegisterForm()

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
    return render(request, "registration/login.html", {"form": form})

def loginSuccess(response):
    return redirect("main")
    