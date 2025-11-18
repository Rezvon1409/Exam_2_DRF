from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ("worker", "Worker"),
        ("employer", "Employer"),
    )

    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default="worker")
    phone = models.CharField(max_length=20,blank=True,null=True,unique=True)

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
