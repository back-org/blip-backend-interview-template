# Blip Backend -- Senior Backend Engineer Portfolio Project

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-5.x-green)
![Architecture](https://img.shields.io/badge/Architecture-Clean%20Architecture-black)
![Security](https://img.shields.io/badge/Security-Production%20Ready-red)
![Observability](https://img.shields.io/badge/Observability-Prometheus%20%2B%20Grafana-orange)
![CI/CD](https://img.shields.io/badge/CI-GitHub%20Actions-success)

------------------------------------------------------------------------

## Senior Backend Engineering Showcase

This project is designed to demonstrate the competencies expected from a
**Senior Backend Engineer**:

-   Scalable API architecture
-   Production-grade security practices
-   Observability-first system design
-   Performance-aware implementation
-   Clean and maintainable codebase
-   CI/CD automation
-   Infrastructure readiness

It reflects real-world backend system design beyond tutorial-level
implementations.

------------------------------------------------------------------------

## Architecture Philosophy

This backend follows core engineering principles:

-   Separation of concerns
-   Environment-based configuration
-   Explicit production hardening
-   Infrastructure as code (Docker Compose)
-   Observability built-in (not bolted on)
-   Security by default

High-level architecture:

Client\
↓\
Django REST API (DRF)\
↓\
Service & Domain Layer\
↓\
PostgreSQL (Primary Database)\
↓\
Redis (Caching Layer)\
↓\
Prometheus → Grafana

------------------------------------------------------------------------

## Core Technical Stack

Backend: - Python 3.12 - Django 5 - Django REST Framework - SimpleJWT
(refresh rotation + blacklist)

Infrastructure: - PostgreSQL - Redis - Docker & Docker Compose -
Gunicorn

Observability: - Prometheus metrics - Grafana dashboards - JSON
structured logs - X-Request-ID correlation tracing

Quality & Security: - Ruff - Black - isort - Bandit - pip-audit - GitHub
Actions CI

------------------------------------------------------------------------

## Key Engineering Features

Authentication & Authorization: - JWT authentication - Refresh token
rotation - Blacklist enforcement - Secure cookie support

Security: - HSTS enabled - HTTPS redirect (production) - Content
Security Policy (configurable) - Rate limiting - Secure headers
middleware

Performance: - Database connection reuse (CONN_MAX_AGE) - Redis caching
support - Optimized middleware stack - Pagination enabled by default

Observability: - Health endpoint (`/health/`) - Metrics endpoint
(`/metrics/`) - CSP violation reporting (`/csp-report/`) - Structured
JSON logs for log aggregation systems

------------------------------------------------------------------------

## Local Development Setup

``` bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
pip install -r requirements-dev.txt

cp .env.example .env

python manage.py migrate
python manage.py runserver
```

------------------------------------------------------------------------

## Dockerized Deployment

``` bash
cp .env.example .env
docker compose up --build
```

Monitoring stack:

``` bash
docker compose -f docker-compose.yml -f docker-compose.monitoring.yml up --build
```

Prometheus: http://127.0.0.1:9090\
Grafana: http://127.0.0.1:3001

------------------------------------------------------------------------

## CI/CD Pipeline

The GitHub Actions workflow performs:

-   Static code analysis
-   Formatting checks
-   Django system validation
-   Unit tests execution
-   Security vulnerability scanning
-   Dependency auditing

This ensures reproducibility, reliability, and deployment confidence.

------------------------------------------------------------------------

## Production Deployment Checklist

-   DEBUG=0
-   Strong SECRET_KEY
-   ALLOWED_HOSTS configured
-   HTTPS enforced
-   CSP validated in report-only mode before enforcement
-   Secure cookies enabled
-   Production settings module activated

Example:

``` bash
export DJANGO_SETTINGS_MODULE=djangodemo.settings.production
export DEBUG=0
```

------------------------------------------------------------------------

## Senior-Level Competencies Demonstrated

This project highlights:

-   System design thinking
-   Security-aware backend development
-   Infrastructure integration
-   Performance optimization mindset
-   Observability integration
-   Automation and CI discipline
-   Clean architecture enforcement
-   Production readiness understanding

------------------------------------------------------------------------

## Intended Role Positioning

Designed to support applications for:

-   Senior Backend Engineer
-   Backend Platform Engineer
-   API Architect
-   Cloud Backend Engineer

------------------------------------------------------------------------

## License

Open for portfolio, interview and educational purposes.
