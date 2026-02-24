FROM python:3.13

# Impede que o Python gere arquivos .pyc e permite logs em tempo real
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Instala o Poetry
RUN pip install poetry

# Copia os arquivos de dependência
COPY pyproject.toml poetry.lock /app/

# Configura o Poetry para não criar venv dentro do container (usa a do sistema)
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

# Copia o restante do código
COPY . /app/