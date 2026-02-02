# 🚀 SoloSync
**SoloSync** é uma plataforma de gestão centralizada para freelancers que desejam organizar seus clientes, prazos de projetos e saúde financeira em um só lugar. Desenvolvido com Python e Django.

---

## 📌 Sobre o Projeto

O SoloSync nasceu da necessidade de profissionais autônomos terem uma visão clara do seu fluxo de trabalho. Diferente de ferramentas genéricas de gestão de tarefas, o SoloSync foca em relação **Cliente -> Projeto -> Faturamento**.

### Principais Funcionalidades:
* **Gestão de Clientes:** Cadastro detalhado de contatos e histórico.
* **Controle de Projetos:** Acompanhamento de status (Planejamento, Execução, Concluído).
* **Gestão de Tarefas:** Checklists internas para cada projeto.
* **Dashboard Financeiro:** Visualização rápida de valores a receber e projetos pagos.
* **Geração de Relatórios:** (Em desenvolvimento) Exportação de faturas em PDF.

## 🛠️ Tecnologias Utilizadas

* **Backend:** [Python](https://www.python.org/) 3.x e [Django](https://www.djangoproject.com/)
* **Banco de Dados:** SQLite (Desenvolvimento) / PostgreSQL (Produção)
* **Frontend:** Django Templates + Bootstrap 5
* **Ferramentas:** Django Signals, Decouple (variáveis de ambiente).

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Python 3.10 ou superior
* Pip (Gerenciador de pacotes)

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/PatrickOrnelas/solosync.git](https://github.com/PatrickOrnelas/solosync.git)
   cd solosync

2. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv # Criando o ambiente virtual
   venv\Scripts\activate # Ativando no Windows
   source venv/bin/activate # Ativando no Linux/Mac

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt

4. **Execute as migrações do banco de dados:**
   ```bash
   python manage.py migrate

5. **Inicie o servidor:**
   ```bash
   python manage.py runserver
  Acesse: http://127.0.0.1:8000

---

Desenvolvido por **Patrick Regula Ornelas**