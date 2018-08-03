"""Delete an entry in MyDiary"""
from flask import Flask, Request
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from api.modals.entry import Entry


class DeleteEntry(Resource):
    """Class for DeleteEntry Resource"""

    @jwt_required
    def delete(self, entry_id):
        """Method to delete a diary entry"""
        user_id = get_jwt_identity()

        entry_instance = Entry(entry_id, user_id, None, None, None)

        entry_exists = entry_instance.get_entry_by_id()

        if entry_exists:
            entry_instance.delete_an_entry()

            find_the_entry = entry_instance.get_entry_by_id()

            if not find_the_entry:
                return {
                    "meassge": "The entry has been deleted",
                    "Deleted entry": entry_exists}, 200
        return {
            "message": "Entry with id {} does not exist".format(entry_id)}, 404
