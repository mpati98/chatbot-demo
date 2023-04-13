from flask_restful import Resource
from flask import request


class UpperName(Resource):

    def get(self):
        return {"response": request.args.get("name").upper(), "method": "GET"}

    def post(self):
        return {
            "response": request.args.get("name").upper(),
            "method": "POST"
        }