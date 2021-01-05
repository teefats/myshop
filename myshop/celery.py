import os
from celery import Celery
from django.conf import settings
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

app = Celery('myshop')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

import redis
from django.conf import settings

# connect to redis
r = redis.Redis(host=settings.REDIS_HOST,
port=settings.REDIS_PORT,
db=settings.REDIS_DB)

