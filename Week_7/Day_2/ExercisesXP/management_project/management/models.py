from django.db import models
from django.contrib.auth.models import User



class Department(models.Model):
    name = models.CharField( max_length=50)
    description = models.TextField()
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , blank=True , null=True,related_name='employee_user')
    name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    phone_number = models.CharField( max_length=50)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    department_administrator = models.BooleanField(default=False)
    def __str__(self):
        return self.name
class Project(models.Model):
    name = models.CharField( max_length=50)
    description = models.TextField()
    start_date = models.DateField( auto_now=False, auto_now_add=False)
    end_date = models.DateField( auto_now=False, auto_now_add=False)
    employees = models.ManyToManyField(Employee)
    def __str__(self):
        return self.name
class Task(models.Model):
    name = models.CharField( max_length=50)
    description = models.TextField()
    due_date = models.DateField( auto_now=False, auto_now_add=False)
    completed = models.BooleanField()
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
