"""Post an entry to MyDiary"""
from flask import Flask, Request
import time
import datetime
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from api.modals.entry import Entry
from api.database.db import DatabaseConnection

class PostEntry(Resource):
    """Class for PostEntry resource"""
    parser = reqparse.RequestParser()
    parser.add_argument('title',
                        type=str,
                        required=True,
                        help="This field can not be left blank!"
                        ),
    parser.add_argument('description',
                        type=str,
                        required=True,
                        help="This field can not be left blank!"
                        )

    @jwt_required
    def post(self):
        """Method to post a new diary entry"""
        data = PostEntry.parser.parse_args()
        user_id = get_jwt_identity()
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        entry_instance = Entry(user_id, data["title"], data["description"], timestamp)

        title_exists = entry_instance.get_entry_by_title()

        if not title_exists:
            entry_instance.add_an_entry()
            get_entry = entry_instance.get_entry_by_title()

            if get_entry:
                return {"message": "Entry has been created"}, 201
            return {"message": "Entry not created, please try again"}
        return {"message": "An entry with the same title exists, please try again"}, 400
