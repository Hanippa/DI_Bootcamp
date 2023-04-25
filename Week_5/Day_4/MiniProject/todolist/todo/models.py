from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField(max_length=200)
    def __str__(self):
        return self.name
    

class Todo(models.Model):
    title = models.CharField(max_length=50)
    details = models.CharField(max_length=50)
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateField( auto_now_add=True)
    date_completion = models.DateField(blank=True,null=True)
    deadline_date = models.DateField()
    category = models.ForeignKey("todo.Category" , on_delete=models.CASCADE)
    def __str__(self):
        return self.title