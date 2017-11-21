# -*- coding: utf-8 -*-

from celery import Celery
from common.settings import CeleryConfig, LoggingConfig
import logging, logging.config

# celery
celery_instance = Celery("tasks")
celery_instance.config_from_object(CeleryConfig)

#logging
logging.config.dictConfig(LoggingConfig)


def logging_instance(name='root'):
    return logging.getLogger(name)


