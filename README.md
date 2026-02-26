# DjangoDemo (Blip Backend Interview Template)

Backend API built with **Django 5** + **Django REST Framework**, featuring:

- ✅ Custom user model (email as username)
- ✅ JWT authentication (SimpleJWT)
- ✅ OpenAPI / Swagger (drf-spectacular)
- ✅ Static files with WhiteNoise
- ✅ Health check endpoint
- ✅ Environment-based configuration (`.env`)

---

## Architecture

```
blip-backend-interview-template/
├─ apps/
│  ├─ users/          # custom user model + auth endpoints
│  ├─ pages/          # CMS-like pages/menus
│  ├─ billing/        # billing domain (example)
│  ├─ utils/          # health checks and misc utilities
│  └─ spectacular/    # schema + swagger urls
├─ djangodemo/
│  ├─ settings/
│  │  ├─ base.py
│  │  ├─ development.py
│  │  └─ production.py
│  ├─ urls.py
│  ├─ asgi.py
│  └─ wsgi.py
├─ static/
├─ templates/
├─ manage.py
├─ requirements.txt
└─ .env.example
```

---

## Quickstart (Local)

### 1) Setup virtualenv

```bash
python -m venv venv
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Configure environment

```bash
cp .env.example .env
```

> ⚠️ Never commit `.env`. It must stay local / in secret managers.

### 4) Migrate + run

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

API base: `http://127.0.0.1:8000/`

---

## API Documentation (Swagger / OpenAPI)

- Schema: `/schema/`
- Swagger UI: exposed by `apps.spectacular` (see its urls)

---

## Health check

- `GET /health/` → `{ "status": "ok", "timestamp": "..." }`

Useful for Docker/Kubernetes/Load balancers.

---

## Security Notes (Production)

The `production` settings enable:

- HTTPS redirect
- Secure cookies (session + CSRF)
- HSTS (30 days starter value)
- Clickjacking protection (`X_FRAME_OPTIONS=DENY`)
- Safer headers (`nosniff`, referrer policy)

**You must** set these environment variables correctly:

- `SECRET_KEY` (strong random)
- `ALLOWED_HOSTS` (comma-separated)
- `CORS_ALLOWED_ORIGINS` (comma-separated, only your frontends)

---

## Performance Notes

- DB connections use `CONN_MAX_AGE=60` (keeps connections warm)
- Pagination is enabled by default (prevents huge responses)
- Basic throttling limits are enabled to reduce abuse
- Redis cache is configured via `REDIS_URL` (optional)

---

## Testing

```bash
pytest
# or with Django test runner
python manage.py test
```

---

## Environment variables

See `.env.example` for the full list.

Minimal required for production:

- `DEBUG=False`
- `SECRET_KEY=...`
- `ALLOWED_HOSTS=api.example.com`
- `DB_ENGINE=postgres`
- `DB_NAME=...`
- `DB_USER=...`
- `DB_PASS=...`
- `DB_HOST=...`
- `DB_PORT=5432`

---

## Common commands

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
```

---

## License

Interview template / educational usage.
