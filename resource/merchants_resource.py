from flask_jwt import jwt_required
from flask_restful import Resource

from merchant_manager import find_all_json


class MerchantsResource(Resource):
    def get(self):
        try:
            merchants = find_all_json()
        except:
            return {'message': 'An error has occurred'}, 400

        return {'payers': merchants}, 200
