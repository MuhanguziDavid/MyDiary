import re
from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import create_access_token
from cryptography.fernet import Fernet

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

        if not re.match(r"\S+", data["username"]):
            return {"message": "Please re-enter your name"}, 400

        if not re.match(r"\S+", data["password"]):
            return {"message": "Please re-enter your password"}, 400

        user_instance = User(data["username"], None, data["password"])
        name_exists = user_instance.get_user_by_name()

        if name_exists:
            key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
            fernet_cipher = Fernet(key)
            unciphered_password = fernet_cipher.decrypt(bytes(name_exists['password'], encoding='utf-8'))
            decoded_password = unciphered_password.decode("utf-8")

            if decoded_password == data["password"]:
                auth_token = create_access_token(name_exists['user_id'])
                return {
                    "user" : name_exists,
                    "auth_token": auth_token,
                    "message": "Logged in Successfully"}, 200
            return {
                "message": "Password incorrect, try again"}, 401
        return {
            "message": "Invalid username or password, try again"}, 401
