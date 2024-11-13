from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from Registration.models import User
from django.views import View

class LoginView(View):
    def get(self, request):
        # Render the login form template
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if both email and password are provided
        if not email or not password:
            messages.error(request, "Please enter both email and password.")
            return redirect('login')

        # Authenticate user using Django's built-in authentication system
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.name}!")
            return redirect('profile')
        else:
            messages.error(request, "Invalid email or password. Please try again.")
            return redirect('login')
