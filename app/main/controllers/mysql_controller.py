from flask import request
from flask_restplus import Resource

from app.main.services.mysql_db_service import mysql_backup
from app.main.utils.mysql_dto import MYSQL

api = MYSQL.api

_request = MYSQL.request


@api.route("api/v1.0/mysql")
class MysqlBackup(Resource):
    @api.expect(_request)
    def post(self):
        data = request.json
        return mysql_backup(data)
