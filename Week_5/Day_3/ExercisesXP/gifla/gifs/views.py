from django.shortcuts import render
from .forms import GifForm , CategoryForm
from .models import Gif , Category
# Create your views here.


# def add_gif(request):
#     if request.method == "POST":
#         form = GifForm(request.POST)
#         if form.is_valid():



def home(request):
    gifs = Gif.objects.all()
    context = {'gifs':gifs}
    return render(request, "home.html",context)
    

def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            new_category = Category(name=name)
            new_category.save()
            return render(request, "home.html")
    else:
        form = CategoryForm()
    return render(request, "add_category.html", {"form": form})


def add_gif(request):
    if request.method == "POST":
        form = GifForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            uploader_name = form.cleaned_data['uploader_name']
            url = form.cleaned_data['url']
            categories = form.cleaned_data['categories']
            new_gif = Gif(title=title, uploader_name=uploader_name, url=url) 
            new_gif.save()
            new_gif.gifs.add(categories)
            return render(request, "add_gif.html", {"form": form})
    else:
        form = GifForm()
    return render(request, "add_gif.html", {"form": form})

def category(request,id):
    gifs = Gifs.objects.filter(id in category)
    return render(request, "home.html", {"gifs": gifs})

def categories(request):
    categories = Category.objects.all()
    return render(request, "categories.html", {"categories": categories})

def gif(request,id):
    gifs = Gif.objects.filter(id = id)
    return render(request, "home.html", {"gifs": gifs})