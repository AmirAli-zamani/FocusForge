from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Correct import of your custom user model
from ..models import CustomUser
from ..forms import RegisterForm, LoginForm, ProfileUpdateForm


def landing_view(request):
    """Landing page to choose between Login and Register"""
    return render(request, "auth/landing.html")


def register_view(request):
    """Handle user registration"""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful.")
            return redirect("user_authentication_module:login")
    else:
        form = RegisterForm()
    return render(request, "auth/register.html", {"form": form})


def login_view(request):
    """Handle user login"""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("user_authentication_module:profile")
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, "auth/login.html", {"form": form})


@login_required
def logout_view(request):
    """Log out the current user"""
    logout(request)
    return redirect("user_authentication_module:login")


@login_required
def profile_view(request):
    """Display user profile"""
    user = request.user  # Already a CustomUser instance
    return render(request, "auth/profile.html", {"user": user})


@login_required
def profile_update_view(request):
    """Update user profile"""
    user = request.user
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("user_authentication_module:profile")
    else:
        form = ProfileUpdateForm(instance=user)
    return render(request, "auth/profile_update.html", {"form": form})
