from flask import request
from flask_restful import Resource, reqparse

from payer import Payer
from payer_manager import find_by_id, save, delete


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
    parser.add_argument('merchant_id',
                        type=int,
                        required=True,
                        help='This field can not be blank!')

    def post(self):
        payer = PayerResource.parser.parse_args()
        payer_id = payer['payer_id']
        if find_by_id(payer_id):
            return {'message': f'the payer_id {payer_id} already exist'}, 400
        save(Payer(payer['payer_id'], payer['extra_data'], payer['merchant_id']))
        return request.get_json(), 201

    def get(self, payer_id):
        payer = find_by_id(payer_id)
        if payer:
            return {'payer_id': payer.id, 'extra_data': payer.extra_data}
        return {'message': f'payer {payer_id} not found'}, 404

    def put(self, payer_id):
        request_payer = PayerResource.parser.parse_args()
        payer = find_by_id(payer_id)
        if payer:
            try:
                payer.extra_data = request_payer['extra_data']
                payer.merchant_id = request_payer['merchant_id']
                save(payer)
                return {'payer_id': payer_id,
                        'extra_data': request_payer['extra_data'],
                        'updated': True}, 200
            except:
                return {'message': 'An error has occurred'}, 500
            # update(Payer(request_payer['payer_id'], request_payer['extra_data']))

        return {'message': f'payer {payer_id} not found'}, 500

    def delete(self, payer_id):
        payer = find_by_id(payer_id)
        if payer:
            try:
                delete(payer)
            except:
                return {'message': 'An error has occurred'}, 400

        return {'payer_id': payer_id, 'deleted': True}, 200 if payer else 404
