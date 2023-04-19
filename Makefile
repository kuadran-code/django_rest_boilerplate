start:
	gunicorn -c core/gunicorn.py core.wsgi

dev:
	python manage.py runserver
