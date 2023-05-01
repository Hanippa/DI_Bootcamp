from django.shortcuts import render
from django.views import generic
from .models import Film , Director
from .forms import AddDirectorForm ,  AddFilmForm,EditFilmForm,EditDirectorForm , Director , Film


# Create your views here.

class homepage(generic.TemplateView):
    template_name = "homepage.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["newfilms"] = Film.objects.filter(release_date = '2023-04-30')
        return context
    

class addFilm(generic.CreateView):
    model = Film
    form_class = AddFilmForm
    template_name = "addfilm.html"


class addDirector(generic.CreateView):
    form_class = AddDirectorForm
    model = Director
    template_name = "addDirector.html"


class editDirector(generic.UpdateView):
    form_class = EditDirectorForm
    model = Director
    template_name = "editDirector.html"
class editFilm(generic.UpdateView):
    form_class = EditFilmForm
    model = Film
    template_name = "editDirector.html"