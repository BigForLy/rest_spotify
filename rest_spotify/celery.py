import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest_spotify.settings')

app = Celery('rest_spotify')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
