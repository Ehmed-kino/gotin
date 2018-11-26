from django import forms


class WordForm(forms.Form):
    name = forms.CharField(max_length=200)
    describtion = forms.CharField(max_length=200)
    meaning = forms.CharField(max_length=200)
