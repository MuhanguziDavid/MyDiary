from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import create_access_token

from api.modals.user import User
from api.database.db import DatabaseConnection

class Log_In(Resource):
    """Class for Login resource"""
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="username field can not be left blank!"
                        ),
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="password field can not be left blank!"
                        )

    def post(self):
        data = Log_In.parser.parse_args()

        user_instance = User(data["username"], None, data["password"])
        name_exists = user_instance.get_user_by_name()

        if name_exists:
            if name_exists['password'] == data['password']:
                auth_token = create_access_token(name_exists['user_id'])
                return {"auth_token": auth_token, "message": "Logged in Successfully"}, 200
            return {"message": "Password incorrect, please re-enter password"}, 401
        return {"message": "Invalid username or password, please try again"}, 401
