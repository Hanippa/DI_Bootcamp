from django.shortcuts import render
import json
# Create your views here.





jsonf = open('animals/info/animals.json')
jsonf = json.load(jsonf)
  

def family(request , id):
    context = {'id':id , 'json':[x for x in jsonf['animals'] if x['family'] == id]}
    return render(request, 'family.html' , context)
def animal(request , id):
    context = {'id':id , 'json':jsonf['animals'][id]}
    return render(request, 'animal.html' , context)
    