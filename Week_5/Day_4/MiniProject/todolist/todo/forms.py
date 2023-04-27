from django import forms
from todo.models import Category , Todo

class DateInput(forms.DateField):
    input_type = 'date'

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        exclude = {'date_completion' , }
        widgets = {
            'deadline_date': forms.DateInput()
        }