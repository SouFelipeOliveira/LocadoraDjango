from django.shortcuts import render, redirect
from .models import Ator, Filme, DvD, Cliente, Locacao
from .forms import *

def home(request):
    return render(request, 'home.html')

def  atores(request):
    data = {}
    data['atores'] = Ator.objects.all()

    if request.method == 'POST':
        form = AtorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('url_atores') 
        else:
            data['form'] = AtorForm()
        return render(request, 'atores.html', data)

def filmes(request):
    filmes = Filme.objects.all()

    form = FilmeFom()
    if request.method == 'POST':
        form = FilmeFom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('url_filmes')
        else:
            filmes = FilmeFom()
    context = {'filmes': filmes, 'form': form}
    return render(request, 'filmes.html', context)


def dvds(request):
    data = {}
    data['dvds'] = DvD.objects.all()

    if request.method == 'POST':
        form = DvDForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('url_dvds')
        else:
            data['dvds'] = DvDForm()
        return render(request, 'dvds.html', data)


def clientes(request):
    data = {}
    data['clientes'] = Cliente.objects.all()

    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('url_clientes')
        else:
            data['clientes'] = ClienteForm()
        return render(request, 'clientes.html', data)

def locacoes(request):
    locacoes = {}
    locacoes = Locacao.objects.all()

    form = LocacaoForm()
    if request.method == 'POST':
        form = LocacaoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('url_locacoes')
        else:
            locacoes = LocacaoForm()
    context = {'form': form, 'locacoes': locacoes}
    return render(request, 'locacoes.html', context)

#atualizaões]

def atualizar_filmes(request):
    data = {}
    # filmes = Filme.objects.all(pk=pk)
        