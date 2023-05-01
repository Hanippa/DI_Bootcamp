
from django.views.generic import DetailView , CreateView
from .models import UserProfile 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import SignUp


class signup_view(CreateView):
    form_class = SignUp
    template_name = 'signup.html'
    success_url = 'homepage'

class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'profile'

# Create your views here.
