from django.shortcuts import render
from .models import Projeto
from django.db.models import Sum

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
