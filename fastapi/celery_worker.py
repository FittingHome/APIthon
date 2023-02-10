import os
import time
from celery import Celery

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")

@celery.task(name="create_task")
def create_task(a, b, c):
    time.sleep(a)
    return b + c

# celeries = Celery('celery_worker', broker='redis://localhost:6379/0')

# @celeries.task()
# def add(timer, x, y):
#     time.sleep(timer)
#     return x + y
