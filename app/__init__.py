from flask_restplus import Api
from flask import Blueprint

from app.main.controllers.mysql_controller import api as mysql_api
from app.main.controllers.mongodb_controller import api as mongodb_api

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='DATABASE BACKUP',
          version='1.0',
          description='Generic Application to take backup of database')

api.add_namespace(mysql_api, path="/")
api.add_namespace(mongodb_api, path="/")
