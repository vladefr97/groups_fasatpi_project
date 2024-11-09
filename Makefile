run:
	uvicorn main:app --reload

install:
	pip install requirements.txt

makemigrations: ## Сделать файл с миграциями. Пример запуска [make makemigrations M="init"]
	alembic revision --autogenerate -m "$(M)"

migrate: ## Применить миграции
	alembic upgrade head