from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .models import Projeto, Cliente, Tarefa
from django.db.models import Sum
from .forms import ProjetoForm

# View de inicio
def index(request):
    return render(request=request, template_name='gestao/index.html')

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

# Views relacionados com clientes
def criar_cliente(request):
    return render(request=request, template_name='gestao/clientes.html')

def listar_clientes(request):
    clientes = Cliente.objects.all()
    print(f"DEBUG: Encontrei {clientes.count()} clientes no banco de dados.")
    context = {
        'clientes' : clientes
    }
    return render(request=request, template_name='gestao/clientes.html', context=context)


def dashboard(request):
    # Consulta todos os projetos
    projetos = Projeto.objects.all()

    # Calcula o faturamento total (soma de todos os projetos)
    faturamento_total = projetos.aggregate(Sum('valor_fechado'))['valor_fechado__sum'] or 0

    # Conta quantos projetos estão em execução
    projetos_ativos = projetos.filter(status='em_andamento').count()

    context = {
        'projetos': projetos,
        'faturamento_total': faturamento_total,
        'projetos_ativos': projetos_ativos,
    }

    return render(request=request, template_name='gestao/dashboard.html', context=context)
