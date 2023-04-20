#!/usr/bin/env bash
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] && [ -n "$DJANGO_SUPERUSER_EMAIL" ] ; then
    (python manage.py createsuperuser --noinput --username adminadmin)
fi

gunicorn -c core/gunicorn.py core.wsgi
