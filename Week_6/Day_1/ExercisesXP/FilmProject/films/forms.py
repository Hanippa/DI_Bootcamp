from django import forms
from .models import Director , Film

class AddFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
        widtgets = {'category' : forms.CheckboxSelectMultiple}
    
class AddDirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
        