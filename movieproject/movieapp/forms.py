from django import forms
from .models import movies
class movie_form(forms.ModelForm):
    class Meta:
        model=movies
        fields=['name','description','year','img']