from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = PhoneNumberField(blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
class Vehicle(models.Model):
    vehicle_type = models.ForeignKey("VehicleType", on_delete=models.CASCADE)
    date_created = models.DateField()
    real_cost = models.IntegerField()
    vehicle_size = models.ForeignKey("VehicleSize", on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.vehicle_type}, {self.real_cost}'
class VehicleType(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name}'
class VehicleSize(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name}'
class Rental(models.Model):
    rental_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null = True , blank = True)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    vehicle = models.ForeignKey("Vehicle", on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.customer} {self.vehicle} {self.rental_date}'
class RentalRate(models.Model):
    daily_rate = models.IntegerField()
    vehicle_type = models.ForeignKey("VehicleType", on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey("VehicleSize", on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.vehicle_type} {self.daily_rate}'