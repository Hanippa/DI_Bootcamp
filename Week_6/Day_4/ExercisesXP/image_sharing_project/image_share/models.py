from django.db import models
from django.contrib.auth.models import User




class Image(models.Model):
    image = models.ImageField(upload_to='media/', height_field=None, width_field=None, max_length=None , null = True , blank=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'{self.title}'
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    images_uploaded = models.IntegerField(default=0)
    def __str__(self) -> str:
        return f'{self.user}'