from django.shortcuts import render
from todo.models import Category , Todo
from todo.forms import TodoForm

# Create your views here.

def todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "todos.html")
    else:
        form = TodoForm()
    return render(request, "todo.html", {"form": form})
def display_todos(request): 
    todos = Todo.objects.all()
    context = {'todos':todos}
    return render(request,'todos.html',context)