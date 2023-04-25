from django import forms
from todo.models import Category , Todo
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        exclude = {'date_completion' , }