from django.shortcuts import render

from .models import Livros

def home(request):
    livros = Livros.objects.all()

    context = {
        'livros':livros
    }

    return render(request, 'lista/home.html', context)
