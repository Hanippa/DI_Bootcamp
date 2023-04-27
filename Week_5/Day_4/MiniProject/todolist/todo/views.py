from django.shortcuts import render
from todo.models import Category , Todo
from todo.forms import TodoForm

# Create your views here.

def add_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "add_todo.html")
    else:
        form = TodoForm()
    return render(request, "todo.html", {"form": form})
def display_todos(request): 
    todos = Todo.objects.all()
    context = {'todos':todos}
    return render(request,'todos.html',context)

def todo(request , id):
    todo = Todo.objects.get(id = id)
    return render(request, 'todo.html' , {'todo':todo})