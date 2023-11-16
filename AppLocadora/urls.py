from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('atores', views.atores, name='url_atores'),
    path('filmes/', views.filmes, name='url_filmes'),
    path('dvd/', views.dvds, name='url_dvds'),
    path('clientes/', views.clientes, name='url_clientes'),
    path('locacoes/', views.locacoes, name='url_locacoes'),
]
