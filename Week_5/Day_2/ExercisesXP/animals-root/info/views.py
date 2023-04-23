from django.shortcuts import render

# Create your views here.

# Create 3 views, corresponding to the following URLs:

#     /family/X, where X is the ID (primary key) of the given family. Should show a list of all animals in that family.
#     /animal/X, where X is the ID (primary key) of the given animal. Should show all the information about the given animal.
#     /animals/ - should show a list of all the animals. When you click on any of the animals in the list, you should be taken to /animal/X (see above).

from django.shortcuts import render
from django.http import HttpRequest
import json
from .models import Animal, Family



def all_animals(request): 
    animals_list = Animal.objects.all()
    context = {'animals': animals_list}

    return render(request, 'animals.html', context)


def animal(request, id: int):
    instance = Animal.objects.get(id=id)
    context = {'animal': instance}
    return render(request, 'animal.html', context)

def family(request, id):
    instance = Animal.objects.filter(family_id = id)
    context = {'family': instance}
    return render(request, 'family.html', context)


# parts 8 and 7 :

# >>> insect = Family.objects.get(name = 'insect') 
# >>> new_family.save()  
# >>> new_family = Family(name = 'reptile') 
# >>> new_family.save()
# >>> new_family = Family(name = 'insect')  
# >>> new_family.save()
# >>> new_family = Family(name = 'arachnid')
# >>> new_family.save()
# >>> new_family = Family(name = 'amphibian') 
# >>> new_family.save()

# >>> new_animal = Animal(name = 'common fly' , legs = 6 , weight = 0.1 , height = 0.1 , speed= 1.2 , family = insect)
# >>> new_animal.save()
# >>> new_animal = Animal(name = 'ladybug' , legs = 6 , weight = 0.1 , height = 0.1 , speed= 1.2 , family = insect)    
# >>> new_animal.save()
# >>> mammel = Family.objects.get(name = 'mammel') 
# >>> new_animal = Animal(name = 'fox' , legs = 6 , weight = 4.1 , height = 4.1 , speed= 19.2 , family = mammel)     
# >>> new_animal.save()