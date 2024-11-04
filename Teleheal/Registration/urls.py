from django.urls import path
from . import views
from .views import register_view

urlpatterns = [
    path('', register_view, name='register'),
    ]