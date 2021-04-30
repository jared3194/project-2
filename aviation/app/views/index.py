from flask import make_response, jsonify
from flask_restful import Resource

class Hello(Resource):
    def get(self):
        return make_response(jsonify(
            {'message': 'Hello'}), 200)