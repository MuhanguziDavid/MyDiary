from flask import Flask, request
from flask_restful import Api, Resource, reqparse

from api.auth.user import User
from api.auth.config import users, entries
from api.database.db import DatabaseConnection


class CreateUser(Resource):
    """Class for CreateUser resource"""
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field can not be left blank!"
                        ),
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="This field can not be left blank!"
                        ),
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field can not be left blank!"
                        ),
    parser.add_argument('confirm_password',
                        type=str,
                        required=True,
                        help="This field can not be left blank!"
                        )

    def post(self):
        """Method to create a new user"""
        data = CreateUser.parser.parse_args()

        con = DatabaseConnection()
        cursor = con.cursor
        
        if data["password"] != data["confirm_password"]:
            return {"status":"fail", "message":"passwords dont match"}, 400
