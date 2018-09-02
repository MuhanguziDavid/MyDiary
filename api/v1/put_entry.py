"""Update an entry in MyDiary"""
import re
import time
from datetime import datetime
from flask import Flask, Request
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from api.modals.entry import Entry


class PutEntry(Resource):
    """Class for PutEntry resource"""
    parser = reqparse.RequestParser()
    parser.add_argument('title',
                        type=str,
                        required=True,
                        help="Title field can not be left blank!"
                        ),
    parser.add_argument('description',
                        type=str,
                        required=True,
                        help="Description field can not be left blank!"
                        )

    @jwt_required
    def put(self, entry_id):
        """Method to modify an entry"""
        data = PutEntry.parser.parse_args()

        if not re.match(r"\S+", data["title"]):
            return {"message": "Please enter the title"}, 400

        if not re.match(r"\S+", data["description"]):
            return {"message": "Please enter the description"}, 400

        user_id = get_jwt_identity()

        current_timestamp = time.time()

        entry_instance = Entry(
            entry_id, user_id, data["title"],
            data["description"], current_timestamp)

        entry_record = entry_instance.get_entry_by_id()

        if not entry_record:
            return {"message": "Entry not found, please try again"}, 404

        current_entry = entry_record[0]
        entry_creation_time = current_entry["creation_time"]
        entry_datetime = datetime.strptime(
            entry_creation_time, '%Y-%m-%d %H:%M:%S')
        entry_creation_timestamp = time.mktime(entry_datetime.timetuple())

        if current_timestamp - entry_creation_timestamp <= 86400:
            title_exists = entry_instance.get_entry_by_title()

            if not title_exists:
                entry_instance.update_an_entry()
                entry_updated = entry_instance.get_entry_by_id()

                if entry_updated:
                    return {
                        "message": "Entry has been updated successfully",
                        "Original entry": entry_record,
                        "Updated entry": entry_updated}, 200
            return {
                "message": "Entry with the same title exists, try again"}, 400
        return {
            "message": "Entry not updated, it was created over 24 hours ago"}, 200
