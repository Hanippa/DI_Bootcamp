from django.db import models

# Create your models here.

class Gif(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    uploader_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(blank=True,null = True)
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)
    gifs = models.ManyToManyField("gifs.Gif",blank=True)

    def __str__(self):
        return self.name
    

    # new_gif = Gif(title = 'python_logo' , url='https://media.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif' , uploader_name = 'Dekel')   