from django import forms

from livrosapp.models import Livros


class LivrosForm(forms.ModelForm):
    class Meta:
        model = Livros
        fields = ('nome', 'autor', 'genero')