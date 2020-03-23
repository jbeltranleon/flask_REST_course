from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from payer_resource import PayerResource
from payers_resource import PayersResource
from user_resource import UserResource
from security import authenticate, identity

# Using __name__ we give a unique name to our Flask app
app = Flask(import_name=__name__)
app.secret_key = 'this_should_be_secret'

# Make the development process easier
api = Api(app=app)

# JWT configuration
jwt = JWT(app=app, authentication_handler=authenticate, identity_handler=identity)  # /auth

api.add_resource(PayerResource, '/payer', endpoint='add_payer')
api.add_resource(PayerResource, '/payer/<int:payer_id>', endpoint='get_or_modify_payer')
api.add_resource(PayersResource, '/payers')
api.add_resource(UserResource, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
