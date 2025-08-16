# Fast Zero (API de Tarefas com FastAPI)

Este projeto é uma API RESTful para gerenciamento de usuários e tarefas, desenvolvida com FastAPI. O projeto foi construído seguindo o curso **[FastAPI do Zero](https://fastapidozero.dunossauro.com/)**, criado e disponibilizado por Eduardo Mendes ([@dunossauro](https://github.com/dunossauro)).

### Tecnologias utilizadas
<div align="center" style="display: inline_block"><br>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" width="50" height="50" alt="Python"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original-wordmark.svg" width="50" height="50" alt="FastAPI"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlalchemy/sqlalchemy-original-wordmark.svg" width="50" height="50" alt="SQLAlchemy"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original-wordmark.svg" width="50" height="50" alt="Docker"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original-wordmark.svg" width="50" height="50" alt="Pytest"/>
</div>

## Executando o projeto

Como executar o projeto localmente.

### Pré-requisitos

* Python 3.11+
* [Poetry](https://python-poetry.org/) para gerenciamento de dependências.
* [Docker](https://www.docker.com/) e Docker Compose (para execução em contêiner).

### Executando localmente

1.  Clone o repositório
    ```sh
    git clone [https://github.com/seu-usuario/fastapi-do-zero](https://github.com/seu-usuario/fastapi-do-zero) # Substitua pelo link do seu repositório
    ```
2.  Na raiz do diretório, crie um arquivo `.env` com as seguintes variáveis de ambiente:
    ```sh
    DATABASE_URL=postgresql+asyncpg://app_user:app_password@localhost:5432/app_db
    SECRET_KEY=sua-chave-secreta-aqui
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```
3.  Instale as dependências do projeto com Poetry
    ```sh
    poetry install
    ```
4.  Execute as migrações do banco de dados com Alembic
    ```sh
    poetry run alembic upgrade head
    ```
5.  Para subir a aplicação (por padrão, ela se encontrará na porta 8000)
    ```sh
    poetry run uvicorn fast_zero.app:app --reload
    ```

### Executando com Docker

Se preferir, você pode executar toda a aplicação (API e banco de dados) usando Docker.

1.  Clone o repositório e crie o arquivo `.env` como nos passos 1 e 2 acima.
2.  Suba os contêineres com Docker Compose:
    ```sh
    docker-compose up -d
    ```
### OBS:
- A documentação interativa da API (gerada pelo Swagger UI) estará disponível em `http://localhost:8000/docs`.
- A documentação alternativa (ReDoc) estará disponível em `http://localhost:8000/redoc`.
