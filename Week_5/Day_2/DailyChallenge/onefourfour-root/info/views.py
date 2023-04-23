from django.shortcuts import render
from .models import Person


# Create your views here.

def persons_name(request , name):
    person = Person.objects.get(name = name)
    context = {'person' : person}
    return render(request, 'persons.html', context)

def persons_phone(request , phone):
    person = Person.objects.get(phone = phone)
    context = {'person' : person}
    return render(request, 'animals.html', context)