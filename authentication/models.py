from django.contrib.auth.models import AbstractUser
from django.db import models

class Investor(AbstractUser):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=30, blank=True)
    apellido = models.CharField(max_length=30, blank=True)
    wallet = models.CharField(max_length=30, blank=True)

    is_active = models.BooleanField(default=True)
    is_investor = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)