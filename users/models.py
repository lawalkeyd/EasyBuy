from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='Email Address', unique=True)
    phone_number = models.CharField(max_length=11, blank=False)
    country = models.CharField(max_length=50, blank=False)
    state = models.CharField(max_length=50, blank=False)
    home_address = models.CharField(max_length=200, blank=False) 
    backup_address = models.CharField(max_length=200, blank=True, null=True)

    objects = CustomUserManager()
    
    def __str__(self):
        return self.first_name
