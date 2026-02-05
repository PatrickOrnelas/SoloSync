from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # URLs para Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    # URLs para Projetos
    path('criar-projeto/', views.criar_projeto, name='criar-projeto'),
    # URLs para Clientes
]