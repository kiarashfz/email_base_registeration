# syntax=docker/dockerfile:1
FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# define django superuser attributes
ENV DJANGO_SUPERUSER_PASSWORD admin
ENV ADMIN_EMAIL admin@admin.admin

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

# preparing django project
CMD python3 manage.py makemigrations --noinput && \
    python3 manage.py migrate --noinput && \
    python3 manage.py collectstatic --noinput && \
    python3 manage.py createsuperuser --email $ADMIN_EMAIL --noinput || true && \
    gunicorn -b 0.0.0.0:8000 email_base_registeration.wsgi
