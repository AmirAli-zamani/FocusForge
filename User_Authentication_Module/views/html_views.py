from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Explicit import of custom user model and forms
from ..models import CustomUser
from ..forms import RegisterForm, LoginForm, ProfileUpdateForm


def landing_view(request):
    """Landing page to choose between Login and Register"""
    return render(request, "auth/register.html")


def register_view(request):
    """Handle user registration and automatically log in the user"""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user

            # Automatically log in the new user
            login(request, user)

            messages.success(request, "Registration successful. You are now logged in.")
            return redirect("task_management_module:task_list")  # Redirect to Task Management page
    else:
        form = RegisterForm()  # Empty form for GET request

    return render(request, "auth/register.html", {"form": form})


def login_view(request):
    """Handle user login and redirect to task list after success"""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()  # Get the authenticated user from the form
            login(request, user)
            return redirect("task_management_module:task_list")  # Redirect to Task Management page
    else:
        form = LoginForm()  # Empty form for GET request

    return render(request, "auth/login.html", {"form": form})


@login_required
def logout_view(request):
    """Log out the current user"""
    logout(request)
    return redirect("user_authentication_module:login")  # Redirect to login page


@login_required
def profile_view(request):
    """Display user profile"""
    return render(request, "auth/profile.html", {"user": request.user})


@login_required
def profile_update_view(request):
    """Update user profile"""
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("user_authentication_module:profile")
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, "auth/profile_update.html", {"form": form})


@login_required
def task_list(request):
    """Display list of user tasks"""
    return render(request, 'Task_Management_Modules/task_list.html')
