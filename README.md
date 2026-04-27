# 🏥 MEDAPI — API de Agendamento Médico

![Python Version](https://img.shields.io/badge/python-3.14-blue?style=for-the-badge&logo=python&logoColor=white)
![Django Version](https://img.shields.io/badge/django-6.0-green?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-3.16-red?style=for-the-badge)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/postgresql-16-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-important?style=for-the-badge)

> API REST para gerenciamento de consultas médicas com autenticação JWT, controle de acesso por papéis (RBAC) e validação automática de conflitos de horário.

**🔗 Deploy:** [https://medapi-u4oq.onrender.com](https://medapi-u4oq.onrender.com)  
**📄 Documentação interativa:** [https://medapi-u4oq.onrender.com/api/docs/](https://medapi-u4oq.onrender.com/api/docs/)

---

## 📌 Sobre o Projeto

A MEDAPI foi desenvolvida para simular o backend de um sistema de agendamento médico. O foco do projeto foi a aplicação de boas práticas de arquitetura REST, separação de responsabilidades por app Django, e controle de acesso granular baseado em papéis de usuário.

---

## ✨ Funcionalidades

- **Autenticação JWT** — login, refresh e registro de usuários via SimpleJWT
- **RBAC** — Admin, Médico e Paciente com permissões e querysets distintos por role
- **Especialidades** — cadastro e listagem de especialidades médicas
- **Médicos** — cadastro com CRM e vínculo à especialidade
- **Pacientes** — cadastro com CPF, telefone e data de nascimento
- **Disponibilidade Médica** — slots de atendimento por dia da semana com duração configurável
- **Consultas** — agendamento com validação de conflito de horário, `end_time` calculado automaticamente e cancelamento mínimo de 24h
- **Fluxo de status** — `scheduled` → `completed` / `canceled`
- **Swagger UI** — documentação interativa gerada automaticamente via drf-spectacular

---

## 🛠️ Tecnologias

| Camada | Tecnologia |
|---|---|
| Backend | Python 3.14 · Django 6.0 |
| API | Django REST Framework 3.16 |
| Autenticação | SimpleJWT |
| Banco de Dados | PostgreSQL 16 (Neon.tech) |
| Containerização | Docker · Docker Compose |
| Servidor | Gunicorn |
| Documentação | drf-spectacular (Swagger UI) |
| Deploy | Render |
| Linting | Flake8 |

---

## 🔐 Credenciais de Demonstração

Para testar a API sem cadastro, use o usuário admin disponível no ambiente de produção:

| Campo | Valor |
|---|---|
| username | `admin` |
| password | `Admin596` |

> Faça `POST /api/v1/auth/login/` com essas credenciais para obter o token JWT e autenticar as demais requisições.

---

## 📋 Endpoints

| Método | Endpoint | Descrição | Auth |
|---|---|---|---|
| POST | `/api/v1/auth/login/` | Obter token JWT | ❌ |
| POST | `/api/v1/auth/refresh/` | Renovar token | ❌ |
| POST | `/api/v1/auth/register/` | Registrar usuário | ❌ |
| GET/POST | `/api/v1/users/` | Listar/criar usuários | ✅ Admin |
| GET/POST | `/api/v1/specialties/` | Listar/criar especialidades | ✅ |
| GET/POST | `/api/v1/doctors/` | Listar/criar médicos | ✅ |
| GET/POST | `/api/v1/patients/` | Listar/criar pacientes | ✅ |
| GET/POST | `/api/v1/availability/` | Listar/criar disponibilidade | ✅ |
| GET/POST | `/api/v1/appointments/` | Listar/criar consultas | ✅ |

> Documentação completa com schemas e exemplos disponível em [`/api/docs/`](https://medapi-u4oq.onrender.com/api/docs/)

---

## 📁 Estrutura do Projeto

```
MEDAPI/
├── app/                  # Configurações principais (settings, urls, wsgi)
├── authentication/       # Autenticação JWT e permissões por role
├── appointments/         # App de consultas
├── availability/         # App de disponibilidade médica
├── doctors/              # App de médicos
├── patients/             # App de pacientes
├── specialties/          # App de especialidades
├── users/                # App de usuários com role customizado
│   └── management/
│       └── commands/
│           └── create_admin.py
├── entrypoint.sh
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── requirements.txt
└── requirements_dev.txt
```

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

Preencha o `.env`:

```env
SECRET_KEY=sua_secret_key_aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://postgres:postgres@db:5432/medapi
```

### 3. Suba os containers

```bash
docker compose up --build
```

### 4. Execute as migrações e crie o admin

```bash
docker compose exec web python manage.py migrate
docker compose exec web python manage.py create_admin --username=admin --email=admin@email.com --password=sua_senha
```

### 5. Acesse a documentação

```
http://localhost:8000/api/docs/
```

---

## 👤 Autor

**João Victor**  
[github.com/joaovictor-sa](https://github.com/joaovictor-sa)
