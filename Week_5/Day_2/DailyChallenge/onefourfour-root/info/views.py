from django.shortcuts import render
from .models import Person


# Create your views here.



def person(request , phone):
    person = Person.objects.get(phone = phone)
    context = {'person' : person}
    return render(request, 'person.html', context)

def persons(request , name):
    person = Person.objects.filter(name = name)
    context = {'person' : person}
    return render(request, 'persons.html', context)
