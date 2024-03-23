from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import RegisterForm, LoginForm


def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to="quotes:root")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotes:root")
    else:
        form = RegisterForm()

    return render(request, "users/signup.html", context={"form": form})


def loginuser(request):
    if request.user.is_authenticated:
        return redirect(to="quotes:root")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(to="quotes:root")
        else:
            messages.error(request, "Username or password didn't match")

    form = LoginForm()
    return render(request, "users/login.html", context={"form": form})


@login_required
def logoutuser(request):
    logout(request)
    return redirect(to="quotes:root")
