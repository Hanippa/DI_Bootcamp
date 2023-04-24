from django.shortcuts import render
from .forms import GifForm
from .models import Gif , Category
# Create your views here.


def add_gif(request):
    if request.method == "POST":
        form = GifForm(request.POST)
        if form.is_valid():

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
            return render(request, "add_gif.html", {"form": form})
    else:
        form = GifForm()
    return render(request, "add_gif.html", {"form": form})


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            new_gif = Category(name=name)
            new_gif.save()
            return render(request, "add_category.html", {"form": form})
    else:
        form = GifForm()
    return render(request, "add_gif.html", {"form": form})