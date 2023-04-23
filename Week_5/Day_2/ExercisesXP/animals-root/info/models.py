from django.db import models

# Create your models here.
# Animal, with properties:

#     id
#     legs – an integer, the number of legs the animal has
#     weight – the average weight of an adult animal of this type
#     height – the average height of an adult animal of this type
#     speed – the maximum speed at which this animal can move
#     family – the family to which this animal belongs. (Must reference the Family model - see below).
class Family(models.Model):
    name = models.CharField(max_length=50)


class Animal(models.Model):
    name = models.CharField(max_length=50)
    legs = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    speed = models.FloatField()
    family = models.ForeignKey(Family, models.SET_NULL , null=True)

# Family, representing an animal group or family, with properties:

#     id
#     name

