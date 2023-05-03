from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .forms import ImageCreationForm
from .models import Image
# Create your views here.

class signup_view(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
class ImageCreateView(generic.CreateView):
    form_class = ImageCreationForm
    model = Image
    template_name = "upload_images.html"
    success_url = '/images'
    def get_initial(self):
        return { 'user' : self.request.user}
class ImageListView(generic.ListView):
    model = Image
    template_name = "images.html"
    context_object_name = "images"
