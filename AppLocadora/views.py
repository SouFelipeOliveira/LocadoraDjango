from django.shortcuts import render, redirect
from .models import Ator, Filme, DvD, Cliente, Locacao
from .forms import *

def home(request):
    return render(request, 'home.html')

def  atores(request):
    ator= Ator.objects.all()
    form = AtorForm()

    if request.method == 'POST':
        form = AtorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('url_atores') 
        else:
            form = AtorForm()
    context = {'ator': ator, 'form': form}
    return render(request, 'atores.html', context)

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


def dvd(request):
    dvds = DvD.objects.all()
    form = DvDForm()
    if request.method == 'POST':
        form = DvDForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('url_dvd')
        else:
            dvds = DvDForm()

    context = {'dvds': dvds, 'form': form}
    return render(request, 'dvd.html', context)


def clientes(request):
    clientes = Cliente.objects.all()
    form = ClienteForm()
    
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('url_clientes')
        else:
            form = ClienteForm()
    context = {'clientes': clientes, 'form': form} 
    return render(request, 'clientes.html', context)

def locacoes(request):
    locacoes = Locacao.objects.all()
    form = LocacaoForm()

    if request.method == 'POST':
        form = LocacaoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('url_locacoes')
        else:
            locacoes = LocacaoForm()

    context = {'locacoes': locacoes, 'form': form}
    return render(request, 'locacoes.html', context)

#atualizaões

def atualiza_filme(request, pk):
    filme = Filme.objects.get(id=pk)
    form = FilmeFom(request.POST or None, instance=filme)

    if form.is_valid():
        form.save()
        return redirect('url_filmes')
    
    context = {'filme': filme, 'form': form}
    return render(request, 'atualiza_filme.html', context)

def atualiza_dvd(request, pk):
    dvd = DvD.objects.get(pk=pk)
    form = DvDForm(request.POST or None, instance=dvd)

    if form.is_valid():
        form.save()
        return redirect('url_dvd')
    
    context = {'dvd': dvd, 'form': form}
    return render(request, 'atualiza_filme.html', context)

def atualiza_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('url_clientes')
    
    context = {'cliente': cliente, 'form': form}
    return render(request, 'atualiza_cliente.html', context)

def atualiza_locacao(request, pk):
    locacao = Locacao.objects.get(pk=pk)
    form = LocacaoForm(request.POST or None, instance=locacao)

    if form.is_valid():
        form.save()
        return redirect('url_locacoes')
    
    context = {'locacao': locacao, 'form': form}
    return render(request, 'atualiza_locacao.html', context)


#Delete

def remover_filme(request, pk):
    filme = Filme.objects.get(pk=pk)
    filme.delete()
    return redirect('url_filmes')

def remover_dvd(request, pk):
    dvd = DvD.objects.get(pk=pk)
    dvd.delete()
    return redirect('url_dvd')

def remover_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    cliente.delete()
    return redirect('url_clientes')

def remover_locacao(request, pk):
    locacao = Locacao.objects.get(pk=pk)
    locacao.delete()
    return redirect('url_locacoes')