from django.shortcuts import render, redirect
from accounts.forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(
                username=username,
                password=password,
            )
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            form.add_error(None, "Incorrect Login Details")

    else:
        form = LoginForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


def user_logout(request):
    logout(request)
    return redirect("login")


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            confirm = form.cleaned_data["password_confirmation"]

            if password == confirm:
                user = User.objects.create_user(username, password)
                login(request, user)
                return redirect("list_projects")
            else:
                form.add_error(None, "the passwords do not match")

    else:
        form = SignupForm()
    context = {"form": form}
    return render(request, "registration/signup.html", context)
