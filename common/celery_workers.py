from celery import Celery
from common.settings import CeleryConfig

celery_instance = Celery("tasks")
celery_instance.config_from_object(CeleryConfig)
