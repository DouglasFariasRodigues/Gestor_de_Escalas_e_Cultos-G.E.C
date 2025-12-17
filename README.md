# ⛪ Sistema de Gestão de Escalas da Igreja

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Django](https://img.shields.io/badge/Django-4.2-blue)
![React](https://img.shields.io/badge/React-18-blue)

Projeto full-stack para automatizar e gerenciar a escala mensal de cultos e obreiros de uma igreja, com backend em Django e frontend em React.

## ✨ Funcionalidades Principais

- **📝 Cadastros Base:** Gerenciamento completo de Obreiros, Locais de culto e Naturezas de Culto (tipos).
- **🗓️ Agenda de Cultos:** Criação e visualização de todos os cultos, com data, hora, local e tipo definidos.
- **📋 Gestão de Escalas:** Atribuição de obreiros para cada culto em uma escala mensal.
- **🚀 Copiar Escala:** Funcionalidade para duplicar a escala de um mês para outro, com mapeamento inteligente de datas e validação de obreiros ativos.
- **🔒 Validação e Integridade:** O sistema impede a alocação de obreiros em horários conflitantes e o uso de cadastros inativos.
- **🔍 Filtros e Buscas:** Pesquise e filtre escalas por mês, ano, local, obreiro, etc.
- **📄 Exportação em PDF:** Geração de um documento PDF da escala mensal, pronto para impressão e distribuição.

## 🛠️ Tecnologias Utilizadas

| Categoria      | Tecnologia                                                              |
|----------------|-------------------------------------------------------------------------|
| ⚙️ **Backend**    | Django, Django REST Framework                                           |
| 🗃️ **Banco de Dados** | PostgreSQL                                                              |
| 🎨 **Frontend**   | React, Vite.js                                                          |
| 💅 **UI/Estilos** | HeroUI, CSS                                                             |
| 📦 **Ambiente**   | Python 3.12+, Node.js 20+                                               |

## 📂 Estrutura do Projeto

```
Study_Space/
├── backend/         # Projeto Django
│   ├── escala/      # App Django principal
│   ├── backend/
│   └── manage.py
├── frontend/        # Projeto React
│   ├── src/
│   └── package.json
└── README.md
```

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e executar o ambiente de desenvolvimento.

### Pré-requisitos

- [Python 3.12+](https://www.python.org/)
- [Node.js 20+](https://nodejs.org/)
- [PostgreSQL](https://www.postgresql.org/) (com um banco de dados criado, ex: `escala_bd`)

### 1. Configuração do Backend

```bash
# 1. Navegue até a pasta do backend
cd backend

# 2. Crie e ative um ambiente virtual
# No Windows
python -m venv venv
.\venv\Scripts\activate
# No Linux/macOS
# python3 -m venv venv
# source venv/bin/activate

# 3. Instale as dependências
pip install django djangorestframework psycopg2-binary django-cors-headers python-dotenv

# 4. Crie um arquivo .env na raiz da pasta 'backend' com base no exemplo abaixo
# Altere os valores conforme a sua configuração do PostgreSQL
```

**Arquivo `.env.example`:**
```env
SECRET_KEY='sua-secret-key-super-segura-aqui'
DEBUG=True
DB_NAME='escala_bd'
DB_USER='postgres'
DB_PASSWORD='sua_senha_do_banco'
DB_HOST='localhost'
DB_PORT='5432'
```

```bash
# 5. Aplique as migrações para criar as tabelas no banco
python manage.py makemigrations
python manage.py migrate

# 6. Inicie o servidor do backend (geralmente em http://127.0.0.1:8000)
python manage.py runserver
```

### 2. Configuração do Frontend

```bash
# 1. Em um novo terminal, navegue até a pasta do frontend
cd frontend

# 2. Instale as dependências
npm install

# 3. Inicie o servidor de desenvolvimento (geralmente em http://localhost:5173)
npm run dev
```

Agora você pode acessar o frontend no seu navegador e começar a usar a aplicação!

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
