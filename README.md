# 🚀 SoloSync - Tutorial de Uso

**SoloSync** é uma plataforma completa de gestão para freelancers organizar clientes, projetos, tarefas e controlar suas finanças em um único lugar. Este guia te ensinará passo a passo como usar todas as funcionalidades!

---

## 📋 Índice
1. [Instalação e Setup](#instalação-e-setup)
2. [Primeira vez acessando](#primeira-vez-acessando)
3. [Gerenciando Clientes](#gerenciando-clientes)
4. [Criando e Acompanhando Projetos](#criando-e-acompanhando-projetos)
5. [Organizando Tarefas](#organizando-tarefas)
6. [Prazos de Entrega](#prazos-de-entrega)
7. [Acompanhando Finanças](#acompanhando-finanças)
8. [Dashboard e Relatórios](#dashboard-e-relatórios)

---

## ⚙️ Instalação e Setup

### Pré-requisitos
* Python 3.10 ou superior
* Pip (Gerenciador de pacotes)
* Git

### Passo 1: Clone o repositório
```bash
git clone https://github.com/PatrickOrnelas/solosync.git
cd solosync
```

### Passo 2: Crie um ambiente virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### Passo 3: Instale as dependências
```bash
pip install -r requirements.txt
```

### Passo 4: Configure o banco de dados
```bash
python manage.py migrate
```

### Passo 5: Inicie o servidor
```bash
python manage.py runserver
```

Acesse a aplicação em: **http://127.0.0.1:8000**

---

## 🎯 Primeira vez acessando

Ao acessar o SoloSync pela primeira vez, você verá a **página inicial (Home)** com um painel de tarefas dividido em três colunas:
- **Planejamento** (tarefas que ainda não começaram)
- **Em Andamento** (tarefas em progresso)
- **Concluídas** (tarefas finalizadas)

Na barra lateral esquerda, encontrará os menus para:
- 📊 Dashboard
- 👥 Clientes
- 📁 Projetos
- ✅ Tarefas

---

## 👥 Gerenciando Clientes

### Como criar um cliente

1. Clique em **Clientes** na barra lateral
2. Clique em **+ Criar Cliente**
3. Preencha os campos:
   - **Nome do Cliente** (obrigatório)
   - **Email** (obrigatório, deve ser válido)
   - **Telefone de Contato** (opcional)
   - **Empresa** (opcional)
4. Clique em **Salvar**

### Como visualizar detalhes de um cliente

1. Na página de clientes, clique no nome do cliente
2. Você verá:
   - Informações completas (nome, email, telefone, empresa)
   - Data de criação do cadastro
   - Opções para editar ou deletar

### Como editar um cliente

1. Acesse a página de detalhes do cliente
2. Clique em **Editar Cliente** (ícone de lápis)
3. Modifique os dados desejados
4. Clique em **Salvar**

### Como deletar um cliente

1. Na página de detalhes ou lista
2. Clique em **Deletar Cliente** (ícone de lixeira)
3. Confirme a ação

---

## 📁 Criando e Acompanhando Projetos

### Como criar um novo projeto

1. Clique em **Projetos** na barra lateral
2. Clique em **+ Criar Projeto**
3. Preencha os dados:
   - **Título do Projeto** (ex: "Site E-commerce")
   - **Descrição** (breve resumo do trabalho)
   - **Data de Início** (quando você começará)
   - **Data de Término** (prazo final do projeto)
   - **Valor do Contrato** (quanto você vai receber)
   - **Cliente** (selecione na lista)
   - **Status** (Planejamento, Em Andamento, Concluído, Cancelado)
4. Clique em **Salvar**

### Como acompanhar um projeto

1. Na lista de projetos, clique no projeto desejado
2. Você verá:
   - Nome, prazo final e valor do contrato
   - **Lista de Tarefas** (todas as tarefas deste projeto)
   - Data de criação e status

### Como editar um projeto

1. Clique no projeto desejado
2. Clique em **Editar Projeto** (ícone de lápis)
3. Modifique os dados
4. Clique em **Salvar**

### Como marcar um projeto como concluído

1. Na página de detalhes do projeto
2. Clique em **Concluir Projeto** (ícone de checkmark)
3. O status passará para "Concluído"

---

## ✅ Organizando Tarefas

### Como criar uma tarefa

1. **Opção 1:** Na página de um projeto, clique em **+ Criar Tarefa**
2. **Opção 2:** No menu lateral, clique em **Tarefas** e crie uma nova

3. Preencha os campos:
   - **Título da Tarefa** (ex: "Criar mockups")
   - **Descrição** (detalhes do que fazer)
   - **Prazo de Entrega** (data limite desta tarefa específica)
   - **Status** (Planejamento, Em Andamento, Concluído, Cancelado)
4. Clique em **Salvar**

### Como visualizar detalhes de uma tarefa

1. Clique no título da tarefa (na lista ou no painel da home)
2. Você verá:
   - Nome da tarefa
   - Data de criação
   - Prazo de entrega
   - Status atual
   - Descrição completa

### Como editar uma tarefa

1. Entre na página de detalhes da tarefa
2. Clique em **Editar Tarefa** (ícone de lápis)
3. Atualize os dados (incluindo prazo se necessário)
4. Clique em **Salvar**

### Como marcar uma tarefa como concluída

1. Na página da tarefa ou na lista dentro de um projeto
2. Clique em **Concluir Tarefa** (ícone de checkmark)
3. A tarefa será movida para a coluna "Concluídas"

### Como deletar uma tarefa

1. Na página de detalhes da tarefa
2. Clique em **Deletar Tarefa** (ícone de lixeira)
3. Confirme a exclusão

---

## 📅 Prazos de Entrega

### O que são prazos de entrega em tarefas?

Diferente do projeto (que tem um prazo geral), cada **tarefa pode ter seu próprio prazo de entrega**. Isso permite uma gestão mais granular dos prazos.

**Exemplo:**
- Projeto: "Site E-commerce" - Prazo: 30 de Março
- Tarefa 1: "Criar mockups" - Prazo: 5 de Março
- Tarefa 2: "Implementar carrinho" - Prazo: 15 de Março
- Tarefa 3: "Testes finais" - Prazo: 28 de Março

### Como definir prazo de entrega em uma tarefa

1. Ao criar ou editar uma tarefa, você verá o campo **Prazo de Entrega**
2. Clique no campo de data e selecione a data limite
3. O prazo é opcional - se não quiser definir, deixe em branco
4. Clique em **Salvar**

### Como visualizar prazos

- **Na tabela de tarefas do projeto:** Há uma coluna "Prazo" que mostra a data de entrega
- **Na página de detalhes da tarefa:** O prazo aparece nos campos informativos
- **No Dashboard:** Há uma seção especial mostrando tarefas vencendo nos próximos 7 dias

### Boas práticas com prazos

✅ Sempre defina prazos para tarefas críticas
✅ Deixe um espaço entre o prazo da tarefa e do projeto
✅ Use prazos para priorizar o trabalho do dia
✅ Monitore diariamente quais tarefas vencem logo

---

## 💰 Acompanhando Finanças

As informações financeiras ficam visíveis no **Dashboard**.

### O que você verá:
- **Valor Total dos Projetos:** Soma de todos os valores fechados
- **Projetos Pagos:** Quantos projetos já foram pagos
- **Projetos em Aberto:** Projetos em andamento e não pagos
- Gráficos visuais do status financeiro

### Como rastrear pagamentos

1. Acesse cada projeto individualmente
2. Você verá se o projeto está marcado como "Pago" ou não
3. Use o Dashboard para ter uma visão geral da sua saúde financeira

---

## 📊 Dashboard e Relatórios

### O que é o Dashboard?

O Dashboard é sua **central de controle**. Nele você verá:

1. **Cards de Resumo:**
   - Total de projetos ativos
   - Projetos finalizados
   - Projetos em andamento
   - Projetos em planejamento
   - Valor total a receber

2. **Gráficos:**
   - **Status dos Projetos:** Gráfico em pizza mostrando a distribuição (Planejamento, Em Andamento, Concluído)
   - **Faturamento Mensal:** (em desenvolvimento)

3. **Prazos da Semana:**
   - Lista de tarefas vencendo nos próximos 7 dias
   - Ajuda a priorizar o trabalho

### Como usar o Dashboard para planejamento

1. Acesse o Dashboard regularmente (antes de iniciar o dia)
2. Verifique as tarefas com prazo próximo
3. Use os gráficos para entender sua carga de trabalho
4. Monitore o valor total a receber para saúde financeira

---

## 💡 Fluxo de Trabalho Recomendado

### Início do dia:
1. Acesse o **Dashboard** e veja tarefas urgentes
2. Identifique tarefas vencendo nos próximos 7 dias
3. Mude o status de tarefas para "Em Andamento"

### Durante o dia:
1. Atualize o status das tarefas conforme progride
2. Adicione tarefas novas se necessário
3. Deixe prazos atualizados

### Final do dia:
1. Marque tarefas concluídas
2. Planeje amanhã consultando o Dashboard
3. Agendar novos projetos se necessário

---

## 💡 Dicas e Boas Práticas

✅ **Sempre defina prazos** - Mantenha a disciplina com datas
✅ **Use status corretamente** - Isso ajuda nos relatórios
✅ **Descreva bem as tarefas** - Facilita foco no que fazer
✅ **Organize por cliente** - Agrupe projetos do mesmo cliente
✅ **Acompanhe o Dashboard** - Revise sua situação financeira regularmente
✅ **Mantenha clientes atualizados** - Use as informações para relatórios

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** [Python](https://www.python.org/) 3.x e [Django](https://www.djangoproject.com/)
* **Banco de Dados:** SQLite (Desenvolvimento) / PostgreSQL (Produção)
* **Frontend:** Django Templates + Bootstrap 5

---

## 📧 Dúvidas ou Sugestões?

Desenvolvido por **Patrick Regula Ornelas**

Se encontrar problemas ou tiver sugestões de melhorias, entre em contato!
