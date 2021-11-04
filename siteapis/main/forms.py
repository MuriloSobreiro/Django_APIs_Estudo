from django import forms

class Pokemon(forms.Form):
    nome = forms.CharField(label="Nome", max_length=200)