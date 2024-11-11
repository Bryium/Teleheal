# models.py

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name
