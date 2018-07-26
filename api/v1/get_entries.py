"""Get all entries in MyDiary"""
from flask import Flask, Request
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import jwt_required

from api.modals.entry import Entry

class EntryList(Resource):
    """Class for EntryList resource"""

    @jwt_required
    def get(self):
        """method to return all entries"""
        entries = Entry.get_all_entries()
        if entries:
            return {"status": "success", "entries": entries}, 200
        else:
            return {"status": "fail", "message": "No entreis in the database"}, 404
