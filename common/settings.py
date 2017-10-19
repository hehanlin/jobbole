# -*- coding: utf-8 -*-
import os

os_env = os.environ


class Config(object):
    """
    web config
    """
    SECRET_KEY = os_env.get('WEB_SECRET', 'secret-key')  # TODO: Change me
    COMMON_PATH = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(COMMON_PATH, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    ASSETS_DEBUG = False
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    MAIL_SERVER = ''
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_DEFAULT_SENDER = ''
    GOOGLE_ANALYTICS = ''


class ProdConfig(Config):
    """Production configuration."""
    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'  # TODO: Change me
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar


class DevConfig(Config):
    """Development configuration."""
    ENV = 'dev'
    DEBUG = True
    DB_NAME = 'dev.db'
    # Put the db file in project root
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
    DEBUG_TB_ENABLED = True
    ASSETS_DEBUG = True  # Don't bundle/minify static assets
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    BCRYPT_LOG_ROUNDS = 1  # For faster tests
    WTF_CSRF_ENABLED = False  # Allows form testing


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
    'disable_existing_loggers': True,

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

class MongoConfig(object):
    HOST = 'localhost'
    PORT = 27017
    DBNAME = 'jobbole'
