
# 📌 Painel Administrativo para Empresa
API desenvolvida com **FastAPI, SQLAlchemy e Pydantic** para gerenciar empresas e suas obrigações acessórias.

## 📋 Funcionalidades
- Cadastro, edição, listagem e remoção de empresas
- Cadastro e gerenciamento de obrigações acessórias
- Conexão assíncrona com banco de dados

---

## 🚀 Tecnologias Utilizadas
- **Python 3.10+**
- **FastAPI** (Framework web)
- **SQLAlchemy + Async** (ORM para banco de dados)
- **Pydantic** (Validação de dados)
- **Uvicorn** (Servidor ASGI)
- **Poetry** (Gerenciamento de dependências)
- **Render** (Hospedagem da API)

---

## 📦 Como Configurar e Rodar o Projeto

### 1️⃣ Clonar o Repositório
```sh
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2️⃣ Criar um ambiente virtual e instalar as dependências com o Poetry
```sh
poetry install
```

### 3️⃣ Configurar as variáveis de ambiente
Crie um arquivo **.env** na raiz do projeto e defina as configurações do banco de dados:

```env
DB_URL=postgresql+asyncpg://usuario:senha@localhost/nome_do_banco
API_V_STR=/api/v1
```

### 4️⃣ Rodar as Migrações (se estiver usando Alembic)
```sh
alembic upgrade head
```

### 5️⃣ Iniciar o Servidor
```sh
poetry run uvicorn app:app --reload
```

A API estará rodando em: **http://127.0.0.1:8000**

---

## 🛠️ Endpoints da API

### ✅ Empresas
- `POST /api/v1/empresas/` → Criar uma empresa
- `GET /api/v1/empresas/` → Listar empresas
- `GET /api/v1/empresas/{id}` → Buscar empresa por ID
- `PUT /api/v1/empresas/{id}` → Atualizar empresa
- `DELETE /api/v1/empresas/{id}` → Remover empresa

### ✅ Obrigações Acessórias
- `POST /api/v1/obrigacoes/` → Criar obrigação acessória
- `GET /api/v1/obrigacoes/` → Listar obrigações
- `PUT /api/v1/obrigacoes/{id}` → Atualizar obrigação
- `DELETE /api/v1/obrigacoes/{id}` → Remover obrigação

---

## 📚 Documentação Automática
Acesse a documentação interativa do FastAPI em:
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🌐 Hospedagem no Render
A API está hospedada no Render, facilitando o deploy automático do projeto. Para acessar o ambiente de produção, basta consultar a URL fornecida pelo Render após o deploy.

---

## 👨‍💻 Autor
**Hugo Leonardo**
📧 Contato: *seu-email@example.com*
