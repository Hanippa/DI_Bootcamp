from django import forms
from .models import Director , Film
from django.contrib.auth.forms import UserCreationForm

class AddFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
        widgets = {'category' : forms.CheckboxSelectMultiple}
    
class AddDirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'

class EditDirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
class EditFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'

