from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    # Relaciona o cliente ao usuário que o cadastrou
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    empresa = models.CharField(max_length=200, blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
class Projeto(models.Model):
    STATUS_CHOICES = [
        ('planejamento', 'Planejamento'),
        ('em_andamento', 'Em Andamento'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='projetos')
    data_inicio = models.DateField()
    prazo_entrega = models.DateField()
    valor_fechado = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planejamento')
    pago = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
    
class Tarefa(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='tarefas')
    titulo = models.CharField(max_length=200)
    data_criacao = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(auto_now_add=True)
    prazo_entrega = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=Projeto.STATUS_CHOICES, default='planejamento')

    def __str__(self):
        # inclui informação de prazo se presente
        if self.prazo_entrega:
            return f"{self.projeto.titulo} - {self.descricao} (prazo {self.prazo_entrega})"
        return f"{self.projeto.titulo} - {self.descricao}"