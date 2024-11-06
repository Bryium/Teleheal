# Login/views.py
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login  # Import authenticate and login
from Registration.models import User  # Assuming you're using a custom User model

class LoginView(View):
    def get(self, request):
        # Render the login form template
        return render(request, 'login.html')

    def post(self, request):
        # Retrieve data from the form
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if user exists and password matches
        try:
            user = User.objects.get(email=email)
            if user.password == password:  # In production, compare hashed passwords instead
                login(request, user)  # Log in the user
                return redirect('home')  # Redirect to the home app on successful login
            else:
                messages.error(request, "Invalid password.")
                return redirect('login')  # Redirect back to login page
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            return redirect('login')  # Redirect back to login page
