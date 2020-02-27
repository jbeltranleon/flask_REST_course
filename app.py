from flask import Flask, request
from flask_restful import Resource, Api

# Using __name__ we give a unique name to our Flask app
app = Flask(__name__)

# Make the development process easier
api = Api(app)

# The payer storage
payers = []


# Resource: Represents Entities
class Payer(Resource):
    def post(self):
        # If request.get_json is null return none using silent
        payers.append(request.get_json(silent=True))
        return request.get_json(), 201


class PayerModify(Resource):
    def get(self, payer_id):
        for payer in payers:
            if payer['payer_id'] == payer_id:
                return payer
            else:
                return {'payer_id': None}, 404

    def put(self, payer_id):
        request_payer = request.get_json()
        for payer in payers:
            if payer['payer_id'] == payer_id:
                payers.remove(payer)
                payers.append(request_payer)
                return {'payer_id': payer_id, 'updated': True}, 200
            else:
                return {'payer_id': None}, 404

    def delete(self, payer_id):
        for payer in payers:
            if payer['payer_id'] == payer_id:
                payers.remove(payer)
                return {'payer_id': payer_id, 'deleted': True}, 200
            else:
                return {'payer_id': None}, 404


class PayerList(Resource):
    def get(self):
        return {'payers': payers}, 200


api.add_resource(Payer, '/payer')
api.add_resource(PayerModify, '/payer/<int:payer_id>')
api.add_resource(PayerList, '/payers')

app.run(port=5000, debug=True)
