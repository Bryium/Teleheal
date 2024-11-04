# registration/views.py

from django.shortcuts import render, redirect
from django.views import View
from .models import User

class RegistrationView(View):
    def get(self, request):
        # Render the registration form template
        return render(request, 'register.html')

    def post(self, request):
        # Retrieve data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        country = request.POST.get('country')

        # Save the new user to the database
        user = User(
            name=name,
            email=email,
            password=password,  # Ideally, hash the password for security
            age=age,
            gender=gender,
            country=country
        )
        user.save()

        # Redirect to the login page after successful registration
        return redirect('login')  # This should be the name of your login URL
