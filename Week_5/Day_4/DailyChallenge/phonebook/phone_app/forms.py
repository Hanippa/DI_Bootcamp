from django import forms
from todo.models import Person,Profile,Language
class onefourForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
