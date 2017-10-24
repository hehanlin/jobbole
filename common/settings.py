# -*- coding: utf-8 -*-

import os

os_env = os.environ


class Config(object):
    COMMON_PATH = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(COMMON_PATH, os.pardir))
    DATABASE_URL = "postgresql+pool://postgres:he@localhost:5432/jobbole"


class CeleryConfig(object):
    BROKER_URL = 'redis://he@127.0.0.1:6379/0'  # 指定 Broker
    CELERY_RESULT_BACKEND = 'redis://he@127.0.0.1:6379/1'  # 指定 Backend
    CELERY_TIMEZONE = 'Asia/Shanghai'  # 指定时区，默认是 UTC
    CELERY_ENABLE_UTC = True
    CELERY_TASK_SERIALIZER = 'msgpack'  # 任务序列化和反序列化 ls: json yaml msgpack pickle(不推荐)
    CELERY_RESULT_SERIALIZER = 'json'  # 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON
    CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24  # 任务过期时间，不建议直接写86400，应该让这样的magic数字表述更明显
    CELERY_IMPORTS = (  # 指定导入的任务模块
    )

# logging
LoggingConfig = {
    'version': 1,

    'formatters': {
        'default': {
            'format': '%(asctime)s- %(module)s:%(lineno)d [%(levelname)1.1s] %(name)s: %(message)s',
            'datefmt': '%Y/%m/%d %H:%M:%S'
        },
    },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'formatter': 'default',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'WARNING',
            'formatter': 'default',
            'class': 'logging.FileHandler',
            'filename': Config.PROJECT_ROOT+'/jobbole_log.log',
            'encoding': 'utf8'
        }
    },

    'loggers': {
        'root': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False,
        }
    },
}
