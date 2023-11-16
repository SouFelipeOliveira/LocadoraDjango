from django import forms
from .models import Ator, Genero, Filme, DvD, Cliente, Locacao

class AtorForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    sobrenome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    pais_origem = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Ator
        fields = ('__all__')

class GeneroForm(forms.ModelForm):
    genero = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Genero
        fields = ('__all__')

class FilmeFom(forms.ModelForm):
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    genero = forms.ModelMultipleChoiceField(queryset=Genero.objects.all(), widget=forms.SelectMultiple(attrs={'type': 'checkbok','class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'type': 'text', 'class': 'form-control'}))
    data_lancamento = forms.DateField(widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}))
    ator = forms.ModelMultipleChoiceField(queryset=Ator.objects.all(), widget=forms.SelectMultiple(attrs={'type':'checkbok','class': 'form-control'}))

    class Meta:
        model = Filme
        fields = ('__all__')

class DvDForm(forms.ModelForm):
    filme = forms.ModelChoiceField(required=False, queryset=Filme.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    estado = forms.ChoiceField(required=False, choices=DvD.ESTADO_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    disponibilidade = forms.ChoiceField(required=False, choices=DvD.DISPONIBILIDADE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = DvD
        fields = ('filme', 'estado', 'disponibilidade',)

class ClienteForm(forms.ModelForm):
    nome = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(required=False, choices=Cliente.STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    rua = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    numero = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    bairro = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    numero_de_telefone = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'type': 'number','class': 'form-control'}))

    class Meta:
        model = Cliente
        fields = ('nome', 'status', 'rua', 'numero', 'bairro', 'numero_de_telefone',)


class LocacaoForm(forms.ModelForm):
    dvd = forms.ModelChoiceField(queryset=DvD.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    data_do_emprestimo = forms.DateField(widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}))
    status = forms.ChoiceField(choices=Locacao.STATUS_DEVOLUCAO_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    data_de_devolucao = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    valor_pago = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Locacao
        fields = ('dvd', 'cliente', 'data_do_emprestimo', 'status', 'data_de_devolucao', 'valor_pago',)