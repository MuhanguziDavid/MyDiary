from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import create_access_token

from api.modals.user import User
from api.database.db import DatabaseConnection


class CreateUser(Resource):
    """Class for CreateUser resource"""
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="username field can not be left blank!"
                        ),
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="email field can not be left blank!"
                        ),
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="password field can not be left blank!"
                        ),
    parser.add_argument('confirm_password',
                        type=str,
                        required=True,
                        help="confirm_password field can not be left blank!"
                        )

    def post(self):
        """Method to create a new user"""
        data = CreateUser.parser.parse_args()

        con = DatabaseConnection()
        cursor = con.cursor
        dict_cursor = con.dict_cursor
        
        if data["password"] != data["confirm_password"]:
            return {"message":"passwords dont match"}, 400
        
        user_instance = User(data["username"], data["email"], data["password"])
        name_exists = user_instance.get_user_by_name(cursor)

        if not name_exists:
            user_instance.create_user(cursor)
            get_user = user_instance.get_user_by_name(dict_cursor)
            
            if get_user:
                auth_token = create_access_token(get_user['user_id'])
                return {"auth_token": auth_token, "message": "Account Created Successfully"}, 201
            return {"message": "User not registered, please try again"}
        return {"message": "username already exists"}, 400
