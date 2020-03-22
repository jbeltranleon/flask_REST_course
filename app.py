from flask import Flask, request
from flask_restful import Resource, Api, reqparse
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
        payer_id = request.get_json()['payer_id']
        if get_payer(payer_id):
            return {'message': f'the payer_id {payer_id} already exist'}, 400
        # If request.get_json is null return none using silent
        payers.append(request.get_json(silent=True))
        return request.get_json(), 201

    def get(self, payer_id):
        # Next give us the first item on the filter object, or return none
        payer = get_payer(payer_id)
        return payer, 200 if payer else 404

    def put(self, payer_id):
        request_payer = Payer.parser.parse_args()
        payer = get_payer(payer_id)
        if payer:
            payer.update(request_payer)
        return {'payer_id': payer_id, 'updated': True}, 200 if payer else 404

    def delete(self, payer_id):
        payer = get_payer(payer_id)
        payers.remove(payer)
        return {'payer_id': payer_id, 'deleted': True}, 200 if payer else 404


class Payers(Resource):
    @jwt_required()
    def get(self):
        return {'payers': payers}, 200


def get_payer(payer_id):
    return next(filter(lambda x: x['payer_id'] == payer_id, payers), None)


api.add_resource(Payer, '/payer', endpoint='add_payer')
api.add_resource(Payer, '/payer/<int:payer_id>', endpoint='get_or_modify_payer')
api.add_resource(Payers, '/payers')

app.run(port=5000, debug=True)
