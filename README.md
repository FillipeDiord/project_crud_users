# CRUD de Usuários

## **Descrição**

Este é um sistema simples de Cadastro, Atualização, Listagem e Exclusão de usuários (CRUD), desenvolvido utilizando o framework Django. Ele permite gerenciar usuários com os seguintes campos: **Nome** e **Idade**. O sistema foi projetado com um layout responsivo utilizando **Bootstrap** e possui notificações visuais por **toasts**, garantindo uma experiência de usuário moderna e intuitiva.

---

## **Tecnologias Utilizadas**

- **Python 3.12.0**: Linguagem de programação principal.
- **Django 5.1.7**: Framework web utilizado para construir o backend.
- **Bootstrap 5**: Biblioteca de CSS para estilização e design responsivo.
- **SQLite**: Banco de dados padrão para armazenar informações.

---

## **Instalação e Configuração**

Siga os passos abaixo para instalar as dependências e executar o sistema:

### **Pré-requisitos**

Certifique-se de que você tem as seguintes ferramentas instaladas:

- Python 3.12.0 ou superior
- Gerenciador de pacotes pip
- Virtualenv (opcional, mas recomendado)

---

### **Passos para Instalação**

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/FillipeDiord/project_crud_users.git
   ```
   Abra o projeto apontando para pasta project_crud_users com a sua IDE de preferência

---

2. **Instale as dependências do projeto:**
   Execute o comando abaixo para instalar o Django e outras bibliotecas:
   ```bash
   pip install -r requirements.txt
   ```
---

3. **Caso precise executar as migrations para configurar banco de dados:**
   ```bash
   python .\manage.py makemigrations
   python .\manage.py migrate
   ```
---

4. **Iniciando o servidor:**
   ```bash
   python .\manage.py runserver
   ```
---