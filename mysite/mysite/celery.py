
from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite',  broker='redis://localhost')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    #name of the scheduler

    'add-every-2-seconds': {
        # task name which we have created in tasks.py

        'task': 'add_function',  
        # set the period of running
        
        'schedule': 2.0,
         # set the args 
         
        'args': (16, 16) 
    },
    #name of the scheduler

    'print-name-every-5-seconds': {  
        # task name which we have created in tasks.py

        'task': 'print_msg_with_me',  
        
        # set the period of running

        'schedule': 5.0,  
        # set the args

       'args': ("DjangoPY", )  
    },
}

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
    