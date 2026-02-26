.PHONY: help install dev test lint format precommit docker-up docker-down docker-monitoring

help:
	@echo "Targets:"
	@echo "  install      Install runtime deps"
	@echo "  dev          Run dev server"
	@echo "  test         Run tests"
	@echo "  lint         Run ruff/black/isort checks"
	@echo "  format       Auto-format with ruff/black/isort"
	@echo "  precommit    Install pre-commit hooks"
	@echo "  docker-up    Start docker stack (web+postgres+redis)"
	@echo "  docker-down  Stop docker stack"

install:
	python -m pip install -U pip
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

dev:
	python manage.py migrate
	python manage.py runserver 0.0.0.0:8000

test:
	python manage.py test

lint:
	ruff check .
	ruff format --check .
	black --check .
	isort --check-only .

format:
	ruff check . --fix
	ruff format .
	black .
	isort .

precommit:
	pre-commit install

docker-up:
	docker compose up --build

docker-down:
	docker compose down -v

docker-monitoring:
	docker compose -f docker-compose.yml -f docker-compose.monitoring.yml up --build
