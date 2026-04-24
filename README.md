[Uploading README.md…]()
# 🏥 MEDAPI — API de Agendamento Médico

![Python Version](https://img.shields.io/badge/python-3.14-blue?style=for-the-badge&logo=python&logoColor=white)
![Django Version](https://img.shields.io/badge/django-6.0-green?style=for-the-badge&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-3.16-red?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-important?style=for-the-badge)

A **MEDAPI** é uma API REST para gerenciamento de consultas médicas. Permite o cadastro de médicos, pacientes e especialidades, controle de disponibilidade e agendamento de consultas com validação de conflitos de horário.

O projeto foi construído com foco em boas práticas de arquitetura REST, controle de acesso por papéis (RBAC) e autenticação via JWT.

---

## ✨ Funcionalidades

- **Autenticação JWT** — login, refresh e registro de usuários
- **Controle de Acesso por Role** — Admin, Médico e Paciente com permissões distintas
- **Especialidades** — cadastro e gerenciamento de especialidades médicas
- **Médicos** — cadastro com CRM e vínculo à especialidade
- **Pacientes** — cadastro com CPF, telefone e data de nascimento
- **Disponibilidade Médica** — cadastro de slots de atendimento por dia da semana
- **Consultas** — agendamento com validação de conflito de horário e regras de cancelamento (mínimo 24h de antecedência)
- **Fluxo de status** — `scheduled` → `completed` / `canceled`
- **Documentação automática** — Swagger UI via drf-spectacular

---

## 🛠️ Tecnologias

| Camada | Tecnologia |
|---|---|
| Backend | Python 3.14 · Django 6 |
| API | Django REST Framework |
| Autenticação | SimpleJWT |
| Banco de Dados | PostgreSQL 16 |
| Containerização | Docker · Docker Compose |
| Servidor | Gunicorn |
| Documentação | drf-spectacular (Swagger) |
| Linting | Flake8 |

---

## 📁 Estrutura do Projeto

```
MEDAPI/
├── app/                  # Configurações principais do projeto Django
├── authentication/       # Autenticação JWT e permissões por role
├── appointments/         # App de consultas
├── availability/         # App de disponibilidade médica
├── doctors/              # App de médicos
├── patients/             # App de pacientes
├── specialties/          # App de especialidades
├── users/                # App de usuários com role customizado
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── requirements.txt
└── requirements_dev.txt
```

---

## 📋 Endpoints

| Método | Endpoint | Descrição |
|---|---|---|
| POST | `/api/v1/auth/login/` | Obter token JWT |
| POST | `/api/v1/auth/refresh/` | Renovar token |
| POST | `/api/v1/auth/register/` | Registrar usuário |
| GET/POST | `/api/v1/users/` | Listar/criar usuários |
| GET/POST | `/api/v1/specialties/` | Listar/criar especialidades |
| GET/POST | `/api/v1/doctors/` | Listar/criar médicos |
| GET/POST | `/api/v1/patients/` | Listar/criar pacientes |
| GET/POST | `/api/v1/availability/` | Listar/criar disponibilidade |
| GET/POST | `/api/v1/appointments/` | Listar/criar consultas |

> Documentação completa disponível em `/api/docs/` após subir o projeto.

---

## ⚙️ Como Rodar Localmente

### Pré-requisitos

- [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) instalados

### 1. Clone o repositório

```bash
git clone https://github.com/joaovictor-sa/MEDAPI.git
cd MEDAPI
```

### 2. Configure as variáveis de ambiente

```bash
cp .env.example .env
```

Preencha o `.env` com os valores adequados:

```
SECRET_KEY=sua_secret_key_aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://postgres:postgres@db:5432/medapi
```

### 3. Suba os containers

```bash
docker compose up --build
```

### 4. Execute as migrações

```bash
docker compose exec web python manage.py migrate
```

### 5. Crie o usuário administrador

```bash
docker compose exec web python manage.py create_admin --username=admin --email=admin@email.com --password=sua_senha
```

### 6. Acesse a documentação

```
http://localhost:8000/api/docs/
```

---

## 👤 Autor

**João Victor**
[github.com/joaovictor-sa](https://github.com/joaovictor-sa)
