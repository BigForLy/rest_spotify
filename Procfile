release: python manage.py migrate
web: gunicorn rest_spotify.wsgi --log-file -
celery: celery worker -A rest_spotify -l info -c 4