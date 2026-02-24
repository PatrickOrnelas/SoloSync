from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .models import Projeto, Cliente, Tarefa
from django.db.models import Sum
from .forms import ProjetoForm, TarefaForm, ClienteForm

# View de inicio
def index(request):
    tarefas = Tarefa.objects.all()
    tarefas_em_planejamento = tarefas.filter(status='planejamento')
    tarefas_em_andamento = tarefas.filter(status='em_andamento')
    tarefas_concluidas = tarefas.filter(status='concluido')
    projeto = Projeto.objects.first()  # Pega o primeiro projeto para exibir as tarefas relacionadas
    print(f"DEBUG: Encontrei {tarefas.count()} tarefas no banco de dados.")
    context = {
        'tarefas': tarefas,
        'tarefas_em_planejamento': tarefas_em_planejamento,
        'tarefas_em_andamento': tarefas_em_andamento,
        'tarefas_concluidas': tarefas_concluidas,
        'projeto': projeto
    }
    return render(request=request, template_name='gestao/index.html', context=context)

# Views relacionados com projetos
def listar_projetos(request):
    projetos = Projeto.objects.all()
    print(f"DEBUG: Encontrei {projetos.count()} projetos no banco de dados.")
    context = {
        'projetos' : projetos
    }
    return render(request=request, template_name='gestao/projetos.html', context=context)

def criar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar-projetos')
    else:
        form = ProjetoForm()

    context = {
        'form' : form
    }

    return render(request=request, template_name='gestao/criar_projeto.html', context=context)

def detalhar_projeto(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    context = {
        'projeto' : projeto
    }
    return render(request=request, template_name='gestao/detalhar_projeto.html', context=context)

def deletar_projeto(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()
    return redirect('listar-projetos')

def editar_projeto(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('listar-projetos')
        else:
            print('DEBUG: Formulário inválido ao editar projeto.')
    else:
        form = ProjetoForm(instance=projeto)
    context = {
        'form' : form,
        'projeto' : projeto
    }
    return render(request=request, template_name='gestao/criar_projeto.html', context=context)

def concluir_projeto(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    projeto.status = 'concluido'
    projeto.save()
    return redirect('listar-projetos')

# Views relacionados com tarefas
def criar_tarefa(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.projeto = projeto
            tarefa.save()
            return redirect('detalhar-projeto', projeto_id=projeto_id)
    else:
        form = TarefaForm()
    context = {
        'form' : form,
        'projeto' : projeto
    }
    return render(request=request, template_name='gestao/criar_tarefa.html', context=context)

def deletar_tarefa(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    projeto_id = tarefa.projeto.id
    tarefa.delete()
    return redirect('detalhar-projeto', projeto_id=projeto_id)

def editar_tarefa(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    projeto_id = tarefa.projeto.id
    
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('detalhar-tarefa', tarefa_id=tarefa.id)
        else:
            print('DEBUG: Formulário inválido ao editar tarefa.')
    else:
        form = TarefaForm(instance=tarefa)
    context = {
        'form' : form,
        'tarefa' : tarefa,
        'projeto' : tarefa.projeto
    }
    return render(request=request, template_name='gestao/criar_tarefa.html', context=context)

def detalhar_tarefa(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    context = {
        'tarefa' : tarefa
    }
    return render(request=request, template_name='gestao/detalhar_tarefa.html', context=context)

def concluir_tarefa(request, tarefa_id, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    tarefa = Tarefa.objects.get(id=tarefa_id)
    tarefa.status = 'concluido'
    tarefa.save()
    return redirect('detalhar-projeto', projeto_id=projeto_id)

# Views relacionados com clientes
def listar_clientes(request):
    clientes = Cliente.objects.all()
    print(f"DEBUG: Encontrei {clientes.count()} clientes no banco de dados.")
    context = {
        'clientes' : clientes
    }
    return render(request=request, template_name='gestao/clientes.html', context=context)

def criar_clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar-clientes')
    else:
        form = ClienteForm()
    context = {
        'form': form
    }
    return render(request=request, template_name='gestao/criar_clientes.html', context=context)

def detalhar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    context = {
        'cliente' : cliente
    }
    return render(request=request, template_name='gestao/detalhar_cliente.html', context=context)

def deletar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    cliente.delete()
    return redirect('listar-clientes')

def editar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('detalhar-cliente', cliente_id=cliente_id)
        else:
            print('DEBUG: Formulário inválido ao editar cliente.')
    else:
        form = ClienteForm(instance=cliente)
    context = {
        'form' : form,
        'cliente' : cliente
    }
    return render(request=request, template_name='gestao/criar_clientes.html', context=context)

# View do Dashboard
def dashboard(request):
    # Consulta todos os projetos
    projetos = Projeto.objects.all()
    # Contagem total de projetos
    total_projetos = projetos.count()

    # Valor total dos projetos (soma de todos os valores fechados)
    valor_total = projetos.aggregate(Sum('valor_fechado'))['valor_fechado__sum'] or 0
    
    # Contagem de projetos por status
    contagem_planejamento = projetos.filter(status='planejamento').count()
    contagem_em_andamento = projetos.filter(status='em_andamento').count()
    contagem_concluido = projetos.filter(status='concluido').count()
    
    # Organiza os dados para o gráfico de pizza
    status_labels = ['Planejamento', 'Em Andamento', 'Concluído']
    status_counts = [contagem_planejamento, contagem_em_andamento, contagem_concluido]

    # Calcula o faturamento total (soma de todos os projetos)
    faturamento_total = projetos.aggregate(Sum('valor_fechado'))['valor_fechado__sum'] or 0

    # Conta quantos projetos estão em execução
    projetos_ativos = projetos.filter(status='em_andamento').count()

    context = {
        'projetos': projetos,
        'total_projetos': total_projetos,
        'valor_total': valor_total,
        'total_planejamento': contagem_planejamento,
        'total_em_andamento': contagem_em_andamento,
        'total_concluido': contagem_concluido,
        'status_labels': status_labels,
        'status_counts': status_counts,
        'faturamento_total': faturamento_total,
        'projetos_ativos': projetos_ativos,
    }

    return render(request=request, template_name='gestao/dashboard.html', context=context)
