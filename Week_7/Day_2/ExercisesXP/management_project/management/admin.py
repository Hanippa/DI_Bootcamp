from django.contrib import admin
from .models import Employee , Task , Project , Department

# Register your models here.

admin.site.register(Employee)
admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Department)