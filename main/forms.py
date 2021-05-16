from django import forms
from django.forms import ModelForm
from .models import *


#create a Movie Form:-
class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'imdb', 'image', 'description')
        labels = {
            'name': '',
            'imdb': '',
            'image': '',
            'description': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Input the Movie Name Here'}),
            'imdb': forms.URLInput(attrs={'class':'form-control', 'placeholder':'An IMDb link of the Movie Here..'}),
            'image': forms.URLInput(attrs={'class':'form-control', 'placeholder':'And a LINK to a picture of the Movie, from the Internet, right here!'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Input the Movie Description Here'}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = {"comment", "rating"}

        labels = {
            'comment': '',
            'rating': '',
        }

        widgets = {
            'comment': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Comment'}),
            'rating': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Rating'})
        }
