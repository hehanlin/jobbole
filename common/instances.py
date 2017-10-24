# -*- coding: utf-8 -*-

from celery import Celery
from common.settings import Config, CeleryConfig, LoggingConfig
import logging, logging.config
from playhouse.db_url import connect
from peewee import Model

# celery
celery_instance = Celery("tasks")
celery_instance.config_from_object(CeleryConfig)

# logging
logging.config.dictConfig(LoggingConfig)


def logging_instance(name='root'):
    return logging.getLogger(name)

# database
db = connect(Config.DATABASE_URL)


class BaseModel(Model):
    """
    you also import the BaseModel just to use database
    """
    class Meta:
        database = db



