from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Custom Manager for User
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

# Custom User model extending AbstractBaseUser
class User(AbstractBaseUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True, null=True)

    objects = CustomUserManager()  # Assign the custom manager

    USERNAME_FIELD = 'email'  # Set the email field as the unique identifier
    REQUIRED_FIELDS = ['name']  # Fields required for user creation

    def __str__(self):
        return self.name
