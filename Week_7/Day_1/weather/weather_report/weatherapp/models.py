from django.db import models

TYPE_CHOICES = (
   ('sunny', 'Sunny'),
   ('cloudy', 'Cloudy'),
   ('windy', 'Windy'),
   ('rainy', 'Rainy'),
   ('stormy', 'Stormy'),
)


class Report(models.Model):
    location = models.CharField(max_length=50)
    temprature = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=50 , choices=TYPE_CHOICES)