from datetime import timezone
from django import forms
from .models import Projeto, Cliente, Tarefa

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'descricao', 'data_inicio', 'prazo_entrega', 'valor_fechado', 'cliente', 'status']
        
        # O segredo é usar widgets aqui para manter o código limpo
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'title-input', 'placeholder': 'Título do projeto'}),
            'descricao': forms.Textarea(attrs={'class': 'description-input', 'placeholder': 'Descrição...', 'rows': 3}),
            'data_inicio': forms.DateInput(attrs={'class': 'date1-input', 'type': 'date'}),
            'prazo_entrega': forms.DateInput(attrs={'class': 'date2-input', 'type': 'date'}),
            'valor_fechado': forms.NumberInput(attrs={'class': 'value-input'}),
            'cliente': forms.Select(attrs={'class': 'client-select'}),
            'status': forms.Select(attrs={'class': 'status-select'}),
        }
        
        # Você pode definir os labels aqui também
        labels = {
            'titulo': 'Título do Projeto',
            'prazo_entrega': 'Data de Término',
        }

    def clean(self):
        cleaned_data = super().clean()
        data_inicio = cleaned_data.get('data_inicio')
        prazo_entrega = cleaned_data.get('prazo_entrega')

        if data_inicio and prazo_entrega and data_inicio > prazo_entrega:
            self.add_error('prazo_entrega', 'A data de término deve ser posterior à data de início.')
        
        return cleaned_data # SEMPRE retorne os dados limpos
    
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'empresa']
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'name-input', 'placeholder': 'Nome do cliente'}),
            'email': forms.EmailInput(attrs={'class': 'email-input', 'placeholder': 'Email'}),
            'telefone': forms.TextInput(attrs={'class': 'phone-input', 'placeholder': 'Telefone'}),
            'empresa': forms.TextInput(attrs={'class': 'company-input', 'placeholder': 'Empresa'}),
        }
        
        labels = {
            'nome': 'Nome do Cliente',
            'telefone': 'Telefone de Contato',
        }

        def clean_email(self):
            email = self.cleaned_data.get('email')
            if email and not email.endswith(('@gmail.com', '@yahoo.com', '@hotmail.com', '@outlook.com')):
                raise forms.ValidationError('Por favor, insira um email válido.')
            return email
        
class TarefasForm(forms.Form):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'data_criacao', 'status']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'title-input', 'placeholder': 'Título da tarefa'}),
            'descricao': forms.Textarea(attrs={'class': 'description-input', 'placeholder': 'Descrição...', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'status-select'}),
        }

        labels = {
            'titulo': 'Título da Tarefa',
            'descricao': 'Descrição da Tarefa',
            'status': 'Status da Tarefa',
        }
