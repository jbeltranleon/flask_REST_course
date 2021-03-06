from flask_jwt import jwt_required
from flask_restful import Resource

from payer_manager import find_all_json


class PayersResource(Resource):
    @jwt_required()
    def get(self):
        try:
            payers = find_all_json()
        except:
            return {'message': 'An error has occurred'}, 400

        return {'payers': payers}, 200
