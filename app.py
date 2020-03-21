from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

# Using __name__ we give a unique name to our Flask app
app = Flask(import_name=__name__)
app.secret_key = 'this_should_be_secret'

# Make the development process easier
api = Api(app=app)

# JWT configuration
jwt = JWT(app=app, authentication_handler=authenticate, identity_handler=identity)  # /auth

# The payer storage
payers = []


# Resource: Represents Entities
class Payer(Resource):
    def post(self):
        payer_id = request.get_json()['payer_id']
        if get_payer(payer_id):
            return {'message': f'the payer_id {payer_id} already exist'}, 400
        # If request.get_json is null return none using silent
        payers.append(request.get_json(silent=True))
        return request.get_json(), 201


class PayerModify(Resource):
    def get(self, payer_id):
        # Next give us the first item on the filter object, or return none
        payer = get_payer(payer_id)
        return payer, 200 if payer else {'payer_id': None}, 404

    def put(self, payer_id):
        request_payer = request.get_json()
        payer = get_payer(payer_id)
        payers.remove(payer)
        payers.append(request_payer)
        return {'payer_id': payer_id, 'updated': True}, 200 if payer else {'payer_id': None}, 404

    def delete(self, payer_id):
        payer = get_payer(payer_id)
        payers.remove(payer)
        return {'payer_id': payer_id, 'deleted': True}, 200 if payer else {'payer_id': None}, 404


class PayerList(Resource):
    @jwt_required()
    def get(self):
        return {'payers': payers}, 200


def get_payer(payer_id):
    return next(filter(lambda x: x['payer_id'] == payer_id, payers), None)


api.add_resource(Payer, '/payer')
api.add_resource(PayerModify, '/payer/<int:payer_id>')
api.add_resource(PayerList, '/payers')

app.run(port=5000, debug=True)
