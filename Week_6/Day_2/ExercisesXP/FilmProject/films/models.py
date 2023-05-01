from django.db import models
from accounts.models import UserProfile
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User
from django.utils import timezone

class Country(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    


class Film(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField(auto_now_add=True)
    created_in_country = models.ForeignKey("Country", on_delete=models.CASCADE, related_name = 'created_films')
    available_in_countries = models.ManyToManyField("Country", related_name = 'avilable_films')
    category = models.ManyToManyField("Category")
    director = models.ManyToManyField("Director" , related_name = 'director_film')
    def __str__(self):
        return self.title

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email





