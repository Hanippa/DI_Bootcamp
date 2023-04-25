from django.contrib import admin
from .models import Person, Language, Profile

admin.site.register(Person)
admin.site.register(Language)
admin.site.register(Profile)