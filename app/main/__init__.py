from flask import Flask
from app.main.config import config_env


def create_app(_config_env):
    app = Flask(__name__)
    app.config.from_object(config_env[_config_env])
    return app
