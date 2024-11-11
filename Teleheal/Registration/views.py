import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User  

@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        age = data.get("age")
        gender = data.get("gender")
        country = data.get("country")

        # Simple validation, if required, could be added here
        if not (name and email and password and age and gender and country):
            return JsonResponse({"success": False, "message": "All fields are required."})

        # Save data to the database
        user = User(name=name, email=email, password=password, age=age, gender=gender, country=country)
        user.save()

        return JsonResponse({"success": True})
    return JsonResponse({"success": False, "message": "Invalid request method"})
