#! /usr/bin/env bash

python manage.py migrate

gunicorn catalog_backend.wsgi:application --name catalog --bind 0.0.0.0:8000