from flask import request
from flask_restful import Resource, reqparse

from merchant import Merchant
from merchant_manager import find_by_name, save, delete


class MerchantResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='This field can not be blank!')

    def post(self):
        merchant = MerchantResource.parser.parse_args()
        merchant_name = merchant['name']
        if find_by_name(merchant_name):
            return {'message': f'the merchant {merchant_name} already exist'}, 400
        save(Merchant(**merchant))
        return request.get_json(), 201

    def get(self, name):
        merchant = find_by_name(name)
        if merchant:
            return {'merchant_id': merchant.id, 'name': merchant.name}
        return {'message': f'merchant {name} not found'}, 404

    def delete(self, name):
        merchant = find_by_name(name)
        if merchant:
            try:
                delete(merchant)
            except:
                return {'message': 'An error has occurred'}, 400

        return {'merchant_name': name, 'deleted': True}, 200 if merchant else 404
