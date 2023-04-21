from django.shortcuts import render

# Create your views here.
people_list = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

def people(request):
    sorted_people_list = sorted(people_list, key=lambda d: d['age']) 
    context = {'plist':sorted_people_list , 'id':0}
    return render(request, 'people.html' , context)



def peopleid(request , id):
    context = {'plist':people_list[id-1], 'id':id}
    return render(request, 'people.html' , context)