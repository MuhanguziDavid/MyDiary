"""Get a specific entry in MyDiary"""
from flask import Flask, Request
"""Get a specific entry from MyDiary"""
from flask import Flask, Request
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from api.modals.entry import Entry
from api.database.db import DatabaseConnection

class GetEntry(Resource):
    """Class for GetEntry resource"""

    @jwt_required
    def get(self, entry_id):
        """method to get a specific diary entry"""
        user_id = get_jwt_identity()

        entry_retreived = Entry.get_entry_by_id(user_id, entry_id)

        if entry_retreived:
            return {"status": "success", "entries": entry_retreived}, 200
        return {"status": "fail", "message": "Entry was not found"}, 404
