from __future__ import absolute_import


import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'image_parrotor.settings')

celery_app = Celery('image_parrotor')
celery_app.config_from_object('dajngo.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()