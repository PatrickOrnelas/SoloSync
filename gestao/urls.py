from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # URLs para Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    # URLs para Projetos
    path('projetos/', views.listar_projetos, name='listar-projetos'),
    path('projetos/criar-projeto/', views.criar_projeto, name='criar-projeto'),
    path('projetos/<int:projeto_id>/', views.detalhar_projeto, name='detalhar-projeto'),
    path('projetos/<int:projeto_id>/deletar/', views.deletar_projeto, name='deletar-projeto'),
    # URLs para Clientes
    path('clientes/', views.listar_clientes, name='listar-clientes'),
    # path('clientes/criar-cliente/', views.criar_cliente, name='criar-cliente'),
    # path('clientes/<int:cliente_id>/', views.detalhar_cliente, name='detalhar-cliente'),
    # URLs para Tarefas
    # path('projetos/<int:projeto_id>/tarefas/', views.listar_tarefas, name='listar-tarefas'),
    # path('projetos/<int:projeto_id>/tarefas/criar-tarefa/', views.criar_tarefa, name='criar-tarefa'),
    # path('tarefas/<int:tarefa_id>/', views.detalhar_tarefa, name='detalhar-tarefa'),
]