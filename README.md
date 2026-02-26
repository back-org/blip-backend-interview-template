# 🚀 Blip Backend -- Enterprise-Grade Django API

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-5.0-green)
![DRF](https://img.shields.io/badge/DRF-REST-red)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![CI](https://img.shields.io/badge/CI-GitHub_Actions-black)

Production-ready Django REST API template designed with:

-   🔐 Advanced security hardening
-   📊 Observability & monitoring
-   🐳 Dockerized infrastructure
-   🧪 CI/CD pipeline
-   🧠 Clean Architecture & best practices
-   ⚡ Performance-oriented configuration

------------------------------------------------------------------------

## 🧭 Overview

This backend template is built with:

-   Django 5
-   Django REST Framework
-   SimpleJWT (rotation + blacklist)
-   PostgreSQL support
-   Redis caching
-   Prometheus metrics
-   Grafana dashboards
-   Structured JSON logging
-   Environment-based configuration
-   Security middleware (CSP / HSTS / Permissions Policy)

Suitable for:

-   Interview projects
-   SaaS MVP
-   Production-ready API starter
-   Backend engineering portfolio

------------------------------------------------------------------------

## 🏗 Architecture

Client\
↓\
Django REST API\
↓\
PostgreSQL\
↓\
Redis Cache\
↓\
Prometheus → Grafana

------------------------------------------------------------------------

## ✨ Key Features

-   Custom User Model (email authentication)
-   JWT Authentication with rotation & blacklist
-   Swagger / OpenAPI documentation
-   Health endpoint: `/health/`
-   Metrics endpoint: `/metrics`
-   CSP Report endpoint: `/csp-report/`
-   Rate limiting protection
-   X-Request-ID correlation
-   Optional profiling with Django Silk

------------------------------------------------------------------------

## ⚙️ Quickstart (Local Development)

``` bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
pip install -r requirements-dev.txt

cp .env.example .env

python manage.py migrate
python manage.py runserver
```

Access:

-   API → http://127.0.0.1:8000/
-   Swagger → /schema/swagger-ui/
-   Health → /health/
-   Metrics → /metrics/

------------------------------------------------------------------------

## 🐳 Docker Setup

``` bash
cp .env.example .env
docker compose up --build
```

Monitoring stack:

``` bash
docker compose -f docker-compose.yml -f docker-compose.monitoring.yml up --build
```

Prometheus → http://127.0.0.1:9090\
Grafana → http://127.0.0.1:3001

------------------------------------------------------------------------

## 🔐 Security Features

-   HSTS enabled
-   Secure cookies
-   HTTPS redirect (production)
-   Content Security Policy (configurable)
-   JWT blacklist
-   Rate limiting
-   Structured JSON logs
-   Request ID correlation

------------------------------------------------------------------------

## 📊 Observability

-   Prometheus metrics
-   Grafana dashboard
-   JSON logs
-   Request tracing
-   Optional performance profiling

------------------------------------------------------------------------

## 🧪 Code Quality & CI

Tooling:

-   Ruff
-   Black
-   isort
-   Bandit
-   pip-audit

CI Pipeline runs:

-   Lint checks
-   Formatting checks
-   Django system check
-   Tests
-   Security scans

------------------------------------------------------------------------

## 🚀 Production Deployment

Use production settings:

``` bash
export DJANGO_SETTINGS_MODULE=djangodemo.settings.production
export DEBUG=0
```

Ensure:

-   Strong SECRET_KEY
-   Proper ALLOWED_HOSTS
-   HTTPS enabled
-   CSP validated in report-only mode first

------------------------------------------------------------------------

## 📈 Performance

-   Database connection pooling (CONN_MAX_AGE)
-   Redis caching support
-   DRF pagination
-   Gunicorn production server

------------------------------------------------------------------------

## 📄 License

Free to use for learning, portfolio and interview purposes.
