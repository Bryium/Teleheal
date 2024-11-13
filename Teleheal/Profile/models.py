from django.db import models
from django.contrib.auth.models import User

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    email = models.EmailField()
    country_of_origin = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username}'s Profile"
