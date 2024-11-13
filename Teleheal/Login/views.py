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

        try:
            user = User.objects.get(email=email)
            if user.password == password:
                login(request, user)
                messages.success(request, f"Welcome, {user.name}!")
                return redirect('profile')
            else:
                messages.error(request, "Invalid password. Please try again.")
                return redirect('login')
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password. Please try again.")
            return redirect('login')
