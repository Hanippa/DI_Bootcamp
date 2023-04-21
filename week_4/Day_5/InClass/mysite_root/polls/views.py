from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# def index(request):
#     return HttpResponse("<h1 style='color:pink;'>Django</h1>")
def index(request):
    context = {'weather' : 'warm'}
    return render(request, 'index.html' , context)