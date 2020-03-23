from flask_jwt import jwt_required
from flask_restful import Resource

from payer_manager import find_all


class PayersResource(Resource):
    @jwt_required()
    def get(self):
        try:
            payers = [{'payer_id': p.id, 'extra_data': p.extra_data} for p in find_all()]
        except:
            return {'message': 'An error has occurred'}, 400

        return {'payers': payers}, 200
