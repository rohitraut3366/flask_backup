import os
import logging
from logging.handlers import TimedRotatingFileHandler

# if not os.path.exists("log/"):
#     os.makedirs("log")
#
# formatter = logging.Formatter(
#     "%(asctime)s - %(levelname)s  %(name)s %(threadName)s :- %(message)s")
#
# handler = TimedRotatingFileHandler(
#     'log/app.log', when="midnight", interval=1, encoding='utf8')
#
# handler.suffix = "%Y-%m-%d_%H-%M-%S"
# handler.setFormatter(formatter)
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)
# logger.addHandler(handler)


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    """
    Development Configuration
    """
    TESTING = True
    DEBUG = True
    ENV = 'development'
    LOG_TYPE = logging.DEBUG
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class TestingConfig(Config):
    """
    Development Configuration
    """
    TESTING = True
    DEBUG = True
    ENV = 'development'
    LOG_FILE = "app.log"
    LOG_TYPE = logging.DEBUG
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(Config):
    TESTING = False
    DEBUG = False
    ENV = 'production'
    LOG_FILE = "app.log"
    LOG_TYPE = logging.DEBUG


config_env = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
