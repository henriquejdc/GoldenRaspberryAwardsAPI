install:
	python3 -m venv .venv
	pip install --upgrade pip
	pip install -r requirements.txt

run:
	ENV=prod PYTHONPATH=. uvicorn app.main:app --reload

test:
	ENV=test PYTHONPATH=. pytest tests

help:
	@echo "Comandos disponíveis:"
	@echo "  make install       - Cria a venv e instala dependências"
	@echo "  make run           - Roda a aplicação com Uvicorn"
	@echo "  make test          - Executa os testes com pytest"
