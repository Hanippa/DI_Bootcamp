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
            for category in categories:
                new_gif.categories.add(category)
            return render(request, "add_gif.html", {"form": form})
    else:
        form = GifForm()
    return render(request, "add_gif.html", {"form": form})

def category(request,id):
    category = Category.objects.get(id = id)
    gifs = category.gifs.all()
    return render(request, "home.html", {"gifs": gifs})

def categories(request):
    categories = Category.objects.all()
    return render(request, "categories.html", {"categories": categories})

def gif(request,id):
    gif = Gif.objects.get(id = id)

    if 'applybtn' in request.POST:
        gif.likes = 22
        gif.save()
    return render(request, "gif.html", {"gif": gif})
    