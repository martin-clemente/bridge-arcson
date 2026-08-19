#!/bin/bash
set -e
python manage.py migrate --noinput
python manage.py collectstatic --noinput
exec gunicorn bridgearcson.wsgi --bind 0.0.0.0:$PORT
