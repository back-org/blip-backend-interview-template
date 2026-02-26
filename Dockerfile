# syntax=docker/dockerfile:1
FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1     PYTHONUNBUFFERED=1

WORKDIR /app

# System deps for psycopg2/mysqlclient (optional)
RUN apt-get update && apt-get install -y --no-install-recommends     build-essential     gcc     libpq-dev     default-libmysqlclient-dev     && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -U pip && pip install --no-cache-dir -r requirements.txt

COPY . /app

# Collect static only in production (optional)
# RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "djangodemo.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2", "--threads", "4", "--timeout", "60"]
