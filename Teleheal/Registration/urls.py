from django.urls import path
from . import views
from .views import register

urlpatterns = [
    path('', register, name='register'),
    ]