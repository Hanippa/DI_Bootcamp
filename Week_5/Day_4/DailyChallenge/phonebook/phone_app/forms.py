from django import forms
from phone_app.models import Person,Profile,Language
class onefourForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = {'name' ,}
