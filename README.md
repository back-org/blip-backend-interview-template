# Blip Backend Interview Template (Django)

Backend API template built with **Django 5** + **Django REST Framework**, ready for real-world usage:
security hardening, environment-based settings, Docker, CI, linting, formatting, monitoring and sensible defaults.

## Features

- Custom user model (email as username)
- JWT support (SimpleJWT) with **refresh rotation + blacklist**
- Auth endpoints:
  - `POST /api/token/` (obtain)
  - `POST /api/token/refresh/`
  - `POST /api/token/verify/`
  - `POST /api/token/blacklist/`
- OpenAPI / Swagger (drf-spectacular)
- Static files with WhiteNoise
- Redis cache (with dev fallback)
- Health check endpoint: `GET /health/`
- **Prometheus metrics** endpoint: `GET /metrics`
- **Request correlation**: `X-Request-ID` header added on every response
- **Rate limiting** (stricter limit on user creation)
- **Extra security headers** middleware (CSP / Permissions-Policy / Referrer-Policy)
- CSP report endpoint: `POST /csp-report/`
- **JSON logs** option for production observability
- Optional profiling with **Django Silk** (`SILK_ENABLED=True`)
- Settings split by environment:
  - `djangodemo.settings.development`
  - `djangodemo.settings.production`

---

## Project structure

```
blip-backend-interview-template/
├─ apps/                       # domain apps
├─ djangodemo/                 # Django project (settings/urls/wsgi/asgi)
├─ monitoring/                 # Prometheus scrape config
├─ .env.example                # environment template (copy to .env)
├─ docker-compose.yml          # web + postgres + redis
├─ docker-compose.monitoring.yml
├─ Dockerfile                  # production-like container
├─ requirements.txt            # runtime deps
├─ requirements-dev.txt        # lint/format/security tooling
└─ .github/workflows/ci.yml    # GitHub Actions
```

---

## Quickstart (local)

### 1) Create & activate a venv

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
```

### 2) Install deps

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 3) Configure env

```bash
cp .env.example .env
```

By default, the project works with **SQLite** (no external services required).

### 4) Run

```bash
python manage.py migrate
python manage.py runserver
```

Open:
- API: `http://127.0.0.1:8000/`
- Swagger UI: `http://127.0.0.1:8000/schema/swagger-ui/`
- Health: `http://127.0.0.1:8000/health/`
- Metrics (Prometheus): `http://127.0.0.1:8000/metrics`

---

## Run with Docker (Postgres + Redis)

1) Copy environment file:

```bash
cp .env.example .env
```

2) Configure Docker/Postgres variables in `.env`:

```env
DB_ENGINE=postgres
DB_HOST=db
DB_PORT=5432
REDIS_URL=redis://redis:6379/0
```

3) Start the stack:

```bash
docker compose up --build
```

The API will be available at `http://127.0.0.1:8000/`.

---

## Monitoring (Prometheus)

This template exposes `/metrics` (via `django-prometheus`).

Run Prometheus alongside the app:

```bash
docker compose -f docker-compose.yml -f docker-compose.monitoring.yml up --build
```

Then open Prometheus:
- `http://127.0.0.1:9090/`

### Grafana (dashboards)

This template ships with a minimal Grafana provisioning setup + an example dashboard.

Start Prometheus + Grafana:

```bash
docker compose -f docker-compose.yml -f docker-compose.monitoring.yml up --build
```

Open Grafana:
- `http://127.0.0.1:3001/` (admin/admin)

---

## Environment variables

See `.env.example`. Common ones:

- `DJANGO_ENV` = `development` or `production`
- `SECRET_KEY` (required)
- `DEBUG` = `1`/`0`
- `ALLOWED_HOSTS` = `localhost,127.0.0.1`
- Database:
  - `DB_ENGINE` = `sqlite` | `postgres` | `mysql`
  - `DB_NAME`, `DB_USER`, `DB_PASS`, `DB_HOST`, `DB_PORT`
- Cache:
  - `REDIS_URL` = `redis://redis:6379/0` (optional; if missing, local memory cache is used)
- Observability:
  - `JSON_LOGS` = `True`/`False`
- Extra security headers:
  - `SECURITY_HEADERS_ENABLED` = `True`/`False`
  - `CSP_ENABLED` = `True`/`False`
  - `CSP_REPORT_ONLY` = `True`/`False`
  - `CSP_POLICY` = CSP policy string
  - `REFERRER_POLICY` / `PERMISSIONS_POLICY`

- Profiling:
  - `SILK_ENABLED` = `True`/`False`

---

## Linting, formatting, pre-commit

```bash
# Checks
make lint

# Auto-format
make format

# Install git hooks
make precommit
```

Tools:
- Ruff (lint + import sorting + formatter)
- Black (formatter)
- isort (import sorting)
- Bandit (basic security checks)
- pip-audit (dependency vulnerability scan)

---

## CI

A GitHub Actions workflow is provided at:
- `.github/workflows/ci.yml`

It runs:
- Ruff lint + format check
- Black/isort checks
- `python manage.py check`
- `python manage.py test`
- Bandit + pip-audit (best-effort)

---

## Security notes

- Never commit `.env` (already ignored)
- Use `djangodemo.settings.production` for deployment (secure cookies, HSTS, HTTPS redirects, etc.)
- Use a strong `SECRET_KEY` and set `DEBUG=0` in production
- Enable CSP progressively (`CSP_REPORT_ONLY=True` first)
- Collect reports at `POST /csp-report/` and tune `CSP_POLICY` before enforcing
- Review `SECURITY.md` for deployment hardening recommendations

---

## Performance notes

- Database connections use `CONN_MAX_AGE` to reuse connections
- Redis cache is supported via `REDIS_URL`
- DRF pagination is enabled by default
- Gunicorn is included for production-style serving (see `Dockerfile`)

---

## License

Use freely for interview/home projects.
