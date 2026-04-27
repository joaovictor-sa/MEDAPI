#!/bin/sh
python manage.py migrate --no-input
python manage.py collectstatic --no-input
python manage.py create_admin --username=admin --email=admin@email.com --password=suasenha
gunicorn app.wsgi:application --bind 0.0.0.0:8000