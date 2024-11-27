# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse

# Home view
def home(request):
    return render(request, 'accounts/home.html')  # Make sure you have a 'home.html' template

# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})  # Make sure you have a 'signup.html' template

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after login
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return redirect('login')  # Redirect back to login if credentials are wrong
    return render(request, 'accounts/login.html')  # Make sure you have a 'login.html' template

# Dashboard view (Only accessible by authenticated users)
@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')  # Make sure you have a 'dashboard.html' template

# Profile view (Only accessible by authenticated users)
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')  # Make sure you have a 'profile.html' template

# Change password view (Only accessible by authenticated users)
@login_required
def change_password(request):
    return render(request, 'accounts/change_password.html')  # Make sure you have a 'change_password.html' template

# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')  # Redirect to login after logout

# Reset password view (if you want to add this feature in the future)
# This is a placeholder for the reset password functionality
def reset_password(request):
    return render(request, 'accounts/reset_password.html')  # Make sure you have a 'reset_password.html' template

