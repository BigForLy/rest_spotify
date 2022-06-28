release: python manage.py migrate
web: gunicorn rest_spotify.wsgi --log-file -
worker: celery -A rest_spotify worker --loglevel=info