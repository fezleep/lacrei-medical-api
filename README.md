Perfeito. Vou manter exatamente seu padrão, sua estrutura e seu jeito direto, só ajustando pequenas coisas de fluidez e coerência — sem deixar com cara de IA.

---

**Lacrei Medical API**

API REST desenvolvida para o desafio técnico da Lacrei Saúde.

O objetivo foi criar um sistema simples para gerenciamento de profissionais de saúde e consultas médicas, atendendo aos requisitos de segurança, autenticação, testes automatizados e preparação para deploy em ambiente real.

> > > > Tecnologias utilizadas <<<<

> Python 3.13
> Django 5
> Django REST Framework
> PostgreSQL
> Poetry
> Docker

> > > > Bibliotecas principais: <<<<

> djangorestframework-simplejwt (JWT)
> django-cors-headers
> drf-spectacular
> psycopg2-binary
> python-dotenv
> dj-database-url

**Escolhi essas ferramentas por serem padrão de mercado e bem consolidadas para construção de APIs seguras e escaláveis.**

---

> > Como rodar localmente <<

Pré-requisitos:

Python 3.13
Poetry

Clonar o repositório:

```
git clone https://github.com/seu-usuario/lacrei-medical-api.git
cd lacrei-medical-api
poetry install
```

Criar arquivo `.env` na raiz:

```
DEBUG=True
SECRET_KEY=sua_chave_secreta
DATABASE_URL=sqlite:///db.sqlite3
```

Rodar migrações:

```
poetry run python manage.py migrate
```

Subir servidor:

```
poetry run python manage.py runserver
```

---

Rodando com Docker

O projeto também pode ser executado via Docker, já configurado com PostgreSQL:

```
docker-compose up --build
```

A aplicação sobe na porta 8000.

---

Autenticação

A API utiliza JWT.

Para gerar o token:

POST
/api/token/

Depois basta enviar no header:

Authorization: Bearer <token>

---

Endpoint obrigatório do desafio

Busca de consultas por profissional:

/api/appointments/by-professional/1/

Esse endpoint retorna todas as consultas vinculadas ao profissional informado.

---

Testes

Foram implementados testes com APITestCase cobrindo:

CRUD de profissionais
CRUD de consultas
Casos de erro

Para rodar:

```
poetry run python manage.py test
```

---

Estrutura

Organizei o projeto em apps separadas (professionals e appointments) para manter as responsabilidades bem definidas.

A API está versionada em /api/.

Utilizei validações nos serializers para evitar dados inválidos antes de persistir no banco.

A autenticação é obrigatória nos endpoints protegidos.

Os logs são registrados em arquivo para facilitar auditoria e análise de erros.

---

CI/CD

Pipeline configurado com GitHub Actions para rodar testes automaticamente em push para as branches main e develop.

---

Rollback

Em caso de problema após deploy:

Revert do commit no branch principal
Nova execução do pipeline
Possibilidade de retornar a imagem Docker anterior

---
