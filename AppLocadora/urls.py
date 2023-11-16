from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('atores', views.atores, name='url_atores'),
    path('filmes/', views.filmes, name='url_filmes'),
    path('dvd/', views.dvd, name='url_dvd'),
    path('clientes/', views.clientes, name='url_clientes'),
    path('locacoes/', views.locacoes, name='url_locacoes'),

    path('atualizar_filme/<int:pk>/', views.atualiza_filme, name='url_atualizaFilme'),
    path('atualizar_dvd/<int:pk>/', views.atualiza_dvd, name='url_atualizaDVD'),
    path('atualizar_cliente/<int:pk>/', views.atualiza_cliente, name='url_atualizaCliente'),
    path('atualizar_locacao/<int:pk>/', views.atualiza_locacao, name='url_atualizaLocacao'),

    path('deletar_filme/<int:pk>/', views.remover_filme, name='url_removerFilme'),
    path('deletar_dvd/<int:pk>/', views.remover_dvd, name='url_removerDVD'),
    path('deletar_cliente/<int:pk>/', views.remover_cliente, name='url_removerCliente'),
    path('deletar_locacao/<int:pk>/', views.remover_locacao, name='url_removerLocacao'),
]
