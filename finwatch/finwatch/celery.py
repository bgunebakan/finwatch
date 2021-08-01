import os
from celery import Celery
from datetime import timedelta

# set the default Django settings module for the 'celery' program.
# this is also used in manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finwatch.settings')


# Get the base REDIS URL, default to redis' default
BASE_REDIS_URL = os.getenv('REDIS_URL', default='redis://127.0.0.1:6379')

app = Celery('finwatch')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.broker_url = BASE_REDIS_URL

# this allows you to schedule items in the Django admin.
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'

# Scrape Finance data every minutes
app.conf.beat_schedule = {
    'scrape-every-minutes': {
        'task': 'scrape_stocks',
        "schedule": timedelta(minutes=1),
    },
}
