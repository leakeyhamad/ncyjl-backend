from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ("youth", "Youth"),
        ("official", "Official"),
        ("supervisor", "Supervisor"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

class YouthProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    national_id = models.CharField(max_length=20, unique=True)
    sub_county = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
