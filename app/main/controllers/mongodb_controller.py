from flask_restplus import Resource

from app.main.services.mongo_db_service import mongo_backup
from app.main.utils.mongodb_dto import MongoDB
from flask import request

api = MongoDB.api


@api.route("api/v1.0/mongodb")
class MongoDB(Resource):
    def post(self):
        data = request.json
        return mongo_backup(data)
