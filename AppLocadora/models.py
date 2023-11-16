from django.db import models

# Create your models here.

class Ator(models.Model):

    nome = models.CharField(max_length=50, blank=True, null=True)
    sobrenome = models.CharField(max_length=50)
    pais_origem  = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nome
    
class Genero(models.Model):
    genero = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.genero

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.ManyToManyField(Genero)
    descricao = models.TextField(max_length=300, blank=True, null=True)
    data_lancamento = models.DateField()
    ator = models.ManyToManyField(Ator)

    def __str__(self):
        return self.titulo
    
class DvD(models.Model):
    NOVO =  'Novo'
    USADO = 'Usado'
    ESTADO_CHOICES = [
        (NOVO, 'Novo'),
        (USADO, 'Usado'),
    ]
    DISPONIVEL = 'Disponivel'
    INDISPONIVEL = 'Indisponivel'
    DISPONIBILIDADE_CHOICES = [
        (DISPONIVEL, 'Disponivel'),
        (INDISPONIVEL, 'Indisponivel'),
    ]


    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    disponibilidade = models.CharField(max_length=20, choices=DISPONIBILIDADE_CHOICES)


    def __str__(self) -> str:
        return str(self.filme)
    
class Cliente(models.Model):
    ATIVO = 'Ativo'
    INATIVO = 'Inativo'
    STATUS_CHOICES = [
        (ATIVO, 'Ativo'),
        (INATIVO, 'Inativo'),
    ]

    nome = models.CharField(max_length=100 )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    rua = models.CharField(max_length=100 )
    numero = models.BigIntegerField(blank=True, null=True)
    bairro = models.CharField(max_length=100)
    numero_de_telefone = models.BigIntegerField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.nome
    
class Locacao(models.Model):
    EM_ABERTO = 'Em aberto'
    FECHADA = 'Fechada'
    STATUS_DEVOLUCAO_CHOICES = [
        (EM_ABERTO, 'Em aberto'),
        (FECHADA, 'Fechada'),
    ]

    dvd = models.ForeignKey(DvD, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_do_emprestimo = models.DateField()
    status = models.CharField(max_length=10, choices= STATUS_DEVOLUCAO_CHOICES)
    data_de_devolucao = models.DateField()
    valor_pago = models.FloatField()

    def __str__(self) -> str:
        return self.cliente
