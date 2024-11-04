from django.urls import path
from . import views
from .views import RegistrationView

urlpatterns = [
    path('', RegistrationView.as_view(), name='register'),
    ]