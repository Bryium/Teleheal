from django.shortcuts import render

def profile(request):
    # Your logic for rendering the profile page
    user_profile = request.user
    return render(request, 'profile.html')
