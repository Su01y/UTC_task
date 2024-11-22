from celery import Celery

from config.config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND

celery = Celery(
    "tasks",
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)

celery.conf.timezone = "UTC"
celery.conf.enable_utc = True
