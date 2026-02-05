from django import forms
from .models import Projeto, Cliente, Tarefa

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        # Campos que o usuário deve informar
        fields = ['titulo', 'descricao', 'data_inicio', 'prazo_entrega', 'valor_fechado', 'status', 'cliente']

        # Widgets que melhoram a interface do formulário
        widgests = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'prazo_entrega': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }