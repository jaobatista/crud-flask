
# CRUD de Usuários - Flask + PostgreSQL

Este projeto implementa um CRUD completo para cadastro de usuários com interface web.

---

## 📋 Funcionalidades

- ✅ **Criar** novo usuário
- ✅ **Visualizar** usuários cadastrados
- ✅ **Editar** usuário existente
- ✅ **Excluir** usuário

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Flask
- Flask-WTF
- Flask-SQLAlchemy
- PostgreSQL
- HTML + CSS + Bootstrap 5

---

## 💻 Como Executar o Projeto

### 1️⃣ Clone o repositório
```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DA_PASTA>
```

### 2️⃣ Crie e ative o ambiente virtual

- **Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

- **Windows (PowerShell):**
```powershell
python -m venv venv
.env\Scripts\Activate.ps1
```

- **Windows (cmd):**
```cmd
python -m venv venv
.env\Scriptsctivate.bat
```

### 3️⃣ Instale as dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure as variáveis de ambiente
Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo:

```
SECRET_KEY=sua_chave_secreta
DATABASE_URL=postgresql://usuario:senha@localhost:5432/crud_usuario
```

> 🔒 **Importante:** Não suba o arquivo `.env` para o GitHub.

### 5️⃣ Crie o banco de dados no PostgreSQL
- Nome: `crud_usuario`
- Usuário e senha conforme configurado no `.env`

### 6️⃣ Crie as tabelas no banco de dados
```bash
python create_db.py
```

### 7️⃣ Execute a aplicação
```bash
python app.py
```

### 8️⃣ Acesse no navegador
```
http://127.0.0.1:5000/
```

---

## 📂 Estrutura do Projeto

```
.
├── app.py              # Aplicação Flask principal
├── config.py           # Configurações da aplicação
├── create_db.py        # Script para criar as tabelas no banco
├── forms.py            # Formulários Flask-WTF
├── models.py           # Modelos do SQLAlchemy
├── requirements.txt    # Dependências do projeto
├── README.md           # Documentação do projeto
├── templates/          # Templates HTML
│   ├── base.html        # Layout base para os templates
│   ├── create.html      # Página para criação de usuário
│   ├── edit.html        # Página para edição de usuário
│   └── index.html       # Página de listagem de usuários
├── static/             # Arquivos estáticos (CSS, JS, imagens)
└── venv/               # Ambiente virtual Python (não versionar)
```

---

## ⚠️ Observações

- As senhas são armazenadas de forma segura com hashing.
- Utilize boas práticas e **NÃO exponha credenciais no código**.
- Em caso de dúvidas, abra uma issue no repositório.

---

## 📌 Entrega

Suba este projeto no GitHub (público) e envie o link para o ambiente virtual da atividade.

---

🚀 **Pronto para usar e testar!**
