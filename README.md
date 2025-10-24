# Desafio_Back_ASCII
# API de Gerenciamento de Produtos

API REST desenvolvida em Python com FastAPI para gerenciar produtos (CRUD completo).

# Sobre o Projeto

Este projeto foi desenvolvido como parte do Desafio Back-End, implementando uma API REST completa para gerenciamento de produtos com operações CRUD (Create, Read, Update, Delete).

## Tecnologias Utilizadas

- **Python 3.10+**
- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy**
- **Pydantic**
- **Uvicorn**

## Arquitetura

O projeto segue uma arquitetura em camadas:

app/
├── config/         # Configurações
├── models/         # Modelos do banco
├── schemas/        # DTOs
├── services/       # Lógica de negocio
├── controllers/    # endpoints da API 
└── main.py         # Aplicação principal


## Pré-requisitos

- Python 3.10 ou superior
- PostgreSQL instalado e rodando
- Git

## Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/MarceloGoncalvesAlves/Desafio_Back_ASCII
cd Desafio_Back_ASCII
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados

**Crie o banco no PostgreSQL:**
```bash
psql -U postgres
CREATE DATABASE produtos_db;
\q
```

**Configure o arquivo .env:**

Crie um arquivo `.env` na raiz do projeto:

**Coloque Nele**
```bash
DATABASE_URL=postgresql://postgres:sua_senha@localhost:5432/produtos_db
```
**Importante:** Substitua `sua_senha` pela senha real do PostgreSQL.


### 5. Execute a aplicação
```bash
uvicorn app.main:app --reload
```

A API estará disponível em: http://localhost:8000

## Documentação da API

Acesse a documentação interativa:
- **Swagger UI:** http://localhost:8000/docs

## Endpoints

- GET /api/produtos → lista todos os produtos 
- GET /api/produtos/{id} → busca produto por id 
- POST /api/produtos → cria novo produto 
- PUT /api/produtos/{id} → atualiza produto 
- DELETE /api/produtos/{id} → remove produto

## Estrutura de Dados

**Produto:**
- `id` (int): Identificador único (gerado automaticamente)
- `nome` (string): Nome do produto (1-100 caracteres)
- `preco` (float): Preço do produto (deve ser maior que 0)
- `categoria` (string): Categoria do produto (1-50 caracteres)

## Validações

A API implementa validações automáticas:
- Nome: obrigatório, 1-100 caracteres
- Preço: obrigatório, maior que 0
- Categoria: obrigatória, 1-50 caracteres

## Funcionalidades Extras


- **Filtros:** Filtro por categoria
- **Validação automática:** DTOs com Pydantic
- **Documentação automática:** Swagger/ReDoc integrados

## Autor
Marcelo Gonçalves Alves
