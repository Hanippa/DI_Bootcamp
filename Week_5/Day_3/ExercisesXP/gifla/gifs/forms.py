from django import forms
from .models import Category


# class GifForm(forms.Form):
#     uploader_name = forms.CharField(label="Uploader name", max_length=30)
#     title = forms.CharField(label="title", max_length=50)
#     url = forms.URLField(required=True)
#     categories = forms.MultipleChoiceField(choices=Category.objects.all(), required=False)
# class CategoryForm(forms.Form):
#     uploader_name = forms.CharField(label="Uploader name", max_length=30)

class GifForm(forms.Form):
    uploader_name = forms.CharField(label="Uploader name", max_length=30)
    title = forms.CharField(label="title", max_length=50)
    url = forms.URLField(required=True)
    # categories = forms.MultipleChoiceField(choices=Category.objects.all().values_list() , required=False)
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(),widget=forms.CheckboxSelectMultiple,label='Categories')

class CategoryForm(forms.Form):
    name = forms.CharField(label="title", max_length=50)
