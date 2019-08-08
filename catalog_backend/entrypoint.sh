#! /usr/bin/env bash

yes | python manage.py collectstatic
python manage.py migrate
## TODO This should be added to the migrations instead of here ##
#python manage.py createsuperuser --noinput --username dan --email dan@dan.dan

gunicorn catalog_backend.wsgi:application --name catalog --capture-output --log-level debug --bind 0.0.0.0:8000