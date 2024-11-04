# Login/views.py
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from Registration.models import User


class LoginView(View):
    def get(self, request):
        # Render the login form template
        return render(request, 'login.html')

    def post(self, request):
        # Retrieve data from the form
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the user exists with matching email and password
        try:
            user = User.objects.get(email=email, password=password)
            # Redirect to home page on successful login
            return redirect('home')
        except User.DoesNotExist:
            # If credentials are incorrect, show an error message
            messages.error(request, "Invalid email or password")
            return redirect('login')
