from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import create_access_token

from api.modals.user import User
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
        dict_cursor = con.dict_cursor
        
        if data["password"] != data["confirm_password"]:
            return {"message":"passwords dont match"}, 400
        
        name_exists = User.get_user_by_name(cursor,data["name"])

        if not name_exists:
            User.create_user(cursor, data["name"], data["email"], data["password"])
            get_user = User.get_user_by_name(dict_cursor, data["name"])
            
            if get_user:
                auth_token = create_access_token(get_user['user_id'])
                return {"auth_token": auth_token, "message": "Account Created Successfully"}, 201
        return {"message": "username already exists"}, 400
