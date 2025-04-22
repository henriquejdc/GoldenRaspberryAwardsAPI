# Golden Raspberry Awards API

## Descrição
API RESTful com FastAPI e SQLAlchemy que lê um CSV de filmes premiados ao iniciar e calcula os produtores indicados 
com maior e menor intervalo entre prêmios consecutivos.

## Requisitos
- Python 3.8+
- `virtualenv` ou python `venv`## Comandos do Makefile

## Setup do ambiente e execução

### Via Makefile
- `make help`       - Lista todos os comandos disponíveis
- `make install`    - Cria o ambiente virtual e instala as dependências
- `make test`       - Executa os testes com pytest
- `make run`        - Inicia a aplicação com Uvicorn

### Via Comandos Manuais

#### Criando o ambiente virtual

```
virtualenv venv # ou python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

### Rodando a aplicação

```
pip install -r requirements.txt
ENV=prod PYTHONPATH=. uvicorn app.main:app --reload
```

### Rodando os testes

```
ENV=test PYTHONPATH=. pytest tests
```

## Documentação

### Estrutura do projeto

```
app/
    data/
        test/movielist.csv -> CSV de exemplo para testes de integração/unitários
        movielist.csv -> CSV que será processado ao rodar aplicação (Substituia esse arquivo para testes manuais)
    database.py -> Conexão com o banco de dados SQLite/SQLAlchemy
    main.py -> Inicialização da aplicação FastAPI
    models.py -> Modelos de dados (SQLAlchemy)
    service.py -> CRUD para manipulação dos dados
    utils.py -> Funções utilitárias de load do .csv na inicialização
tests/
    test_awards.py
```

### Swagger

Acesse o Swagger em `http://localhost:8000/docs` para visualizar a documentação da API.


### Endpoints

- `GET /awards/intervals`: Retorna produtores indicados com maior e menor intervalo entre prêmios consecutivos.

### Exemplo de saída

```json
{
  "min": [
    {
      "producer": "Joel Silver",
      "interval": 1,
      "previousWin": 1990,
      "followingWin": 1991
    }
  ],
  "max": [
    {
      "producer": "Matthew Vaughn",
      "interval": 13,
      "previousWin": 2002,
      "followingWin": 2015
    }
  ]
}
```
