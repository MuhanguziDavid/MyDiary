"""Get all entries in MyDiary"""
from flask import Flask, Request
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from api.modals.entry import Entry
from api.database.db import DatabaseConnection

class EntryList(Resource):
    """Class for EntryList resource"""

    @jwt_required
    def get(self):
        """method to return all entries"""
        user_id = get_jwt_identity()

        con = DatabaseConnection()
        cursor = con.cursor
        dict_cursor = con.dict_cursor

        entries = Entry.get_all_entries(dict_cursor, user_id)
        if entries:
            return {"status": "success", "entries": entries}, 200
        else:
            return {"status": "fail", "message": "No entreis in the database"}, 404
