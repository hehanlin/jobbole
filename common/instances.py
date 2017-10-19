from celery import Celery
from common.settings import CeleryConfig, LoggingConfig, MongoConfig
import logging, logging.config
from mongoengine import connect

# celery
celery_instance = Celery("tasks")
celery_instance.config_from_object(CeleryConfig)

# logging
logging.config.dictConfig(LoggingConfig)
def logging_instance(name='root'):
    return logging.getLogger(name)

# mongoEngine
connect(MongoConfig.DBNAME,
        host=MongoConfig.HOST,
        port=MongoConfig.PORT)
