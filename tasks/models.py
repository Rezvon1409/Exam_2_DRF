from django.db import models
from django.conf import settings
from accounts.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    employer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={"role": "employer"})
    assigned_worker = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,related_name="applied_vacancies",null=True,blank=True,limit_choices_to={"role": "worker"})
    is_filled = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title


class Application(models.Model):
    worker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={"role": "worker"}
    )
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)  
    is_accepted = models.BooleanField(default=False)  
    def __str__(self):
        return f"{self.worker} -> {self.vacancy}"
