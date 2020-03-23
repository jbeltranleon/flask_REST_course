# Resource: Represents Entities
from flask import request
from flask_restful import Resource, reqparse

from payer_manager import find_by_id, create, delete, update


class PayerResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('payer_id',
                        type=int,
                        required=True,
                        help='This field can not be blank!')
    parser.add_argument('extra_data',
                        type=str,
                        required=False,
                        help='This field can not be blank!')

    def post(self, payer_id=None):
        payer = PayerResource.parser.parse_args()
        payer_id = payer['payer_id']
        if find_by_id(payer_id):
            return {'message': f'the payer_id {payer_id} already exist'}, 400
        # If request.get_json is null return none using silent
        create(payer)
        return request.get_json(), 201

    def get(self, payer_id):
        # Next give us the first item on the filter object, or return none
        payer = find_by_id(payer_id)
        if payer:
            return {'payer_id': payer.id, 'extra_data': payer.extra_data}
        return {'message': f'payer {payer_id} not found'}, 404

    def put(self, payer_id):
        request_payer = PayerResource.parser.parse_args()
        payer = find_by_id(payer_id)
        if payer:
            try:
                update(payer_id, request_payer['extra_data'])
                return {'payer_id': payer_id,
                        'extra_data': request_payer['extra_data'],
                        'updated': True}, 200
            except:
                return {'message': 'An error has occurred'}, 400

        return {'message': f'payer {payer_id} not found'}, 404

    def delete(self, payer_id):
        payer = find_by_id(payer_id)
        if payer:
            try:
                delete(payer_id)
            except:
                return {'message': 'An error has occurred'}, 400

        return {'payer_id': payer_id, 'deleted': True}, 200 if payer else 404
