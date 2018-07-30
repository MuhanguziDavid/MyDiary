"""Delete an entry in MyDiary"""
from flask import Flask, Request
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from api.modals.entry import Entry

class DeleteEntry(Resource):
    """Class for DeleteEntry Resource"""
    parser = reqparse.RequestParser()
    parser.add_argument('entry_id',
                        type=int,
                        required=True,
                        help="Entry id field can not be left blank!"
                        )
    
    @jwt_required
    def delete(self):
        """Method to delete a diary entry"""
        data = DeleteEntry.parser.parse_args()
        user_id = get_jwt_identity()

        entry_instance = Entry(data["entry_id"], user_id, None, None, None)

        entry_instance.delete_an_entry()

        find_the_entry = entry_instance.get_entry_by_id()

        if not find_the_entry:
            return {"meassge": "The entry has been deleted"}, 200
        return {"message": "Entry not deleted, please try again"}
