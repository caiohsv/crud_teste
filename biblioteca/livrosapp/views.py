from django.shortcuts import render, redirect
from livrosapp.forms import LivrosForm
from django.contrib.auth.decorators import login_required


from .models import Livros

@login_required
def home(request):
    lista = Livros.objects.all().filter(user=request.user)

    context = {
        'lista':lista
    }

    return render(request, 'lista/home.html', context)

@login_required
def addlivro(request):
    form = LivrosForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            livro = form.save(commit=False)
            livro.user = request.user
            livro.save()
            return redirect('home')

    context = {
        'form':form
    }

    return render(request, 'lista/addlivro.html', context)

@login_required
def editlivro(request, id):
    livro = Livros.objects.get(pk=id)
    
    form = LivrosForm(request.POST or None, instance=livro)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form':form
    }

    return render(request, 'lista/editlivro.html', context)

@login_required
def deletelivro(request, id):
    livro = Livros.objects.get(pk=id)
    livro.delete()

    return redirect('home')
