from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    # path('Registration/success/', views.success, name='success'),
]
