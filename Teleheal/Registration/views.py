from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import User

def register(request):
    if request.method == "POST":
        # Retrieve data from the form
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        country = request.POST.get("country")

        # Simple validation, if required
        if not (name and email and password and age and gender and country):
            return JsonResponse({"success": False, "message": "All fields are required."})

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            return JsonResponse({"success": False, "message": "Email is already registered."})

        # Save data to the database with password hashing
        user = User(name=name, email=email, password=password, age=age, gender=gender, country=country)
        user.set_password(password)
        user.save()

        # Redirect to a success page or render a response
        messages.success(request, "Registration successfully!")
        return redirect('login')

    return render(request, "register.html")
