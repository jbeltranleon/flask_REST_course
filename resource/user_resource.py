import sqlite3

from flask_restful import Resource, reqparse

from user_manager import find_by_username, create


class UserResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='This field cannot be blank')
    parser.add_argument('password', type=str, required=True, help='This field cannot be blank')

    def post(self):

        user = UserResource.parser.parse_args()

        if find_by_username(user['username']):
            return {'message': 'the user already exist'}, 400

        create(user)

        return {'message': 'user created successfully'}, 201
