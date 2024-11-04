from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', login_view, name='login'),
    # path('register/', register_view, name='register'),

    ]