# import logging
# import os
# import configparser
#
# from logging.handlers import TimedRotatingFileHandler
#
# LOG_LEVEL = logging.DEBUG
# config = configparser.ConfigParser()
# config.read(os.getcwd() + "/app/main/config.ini")
#
# if not os.path.exists("log/"):
#     os.makedirs("log")
#
# if config['ENVIRONMENT']['ENV'] == 'PRODUCTION':
#     LOG_LEVEL = logging.INFO
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
# logger.setLevel(LOG_LEVEL)
# logger.addHandler(handler)
