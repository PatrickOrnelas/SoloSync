from django.contrib import admin
from .models import Cliente, Projeto, Tarefa

admin.site.register(Cliente)
admin.site.register(Projeto)
admin.site.register(Tarefa)