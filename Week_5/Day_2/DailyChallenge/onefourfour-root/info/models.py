from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models 
class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    phone = PhoneNumberField(blank=True)
    address = models.CharField(max_length=50)