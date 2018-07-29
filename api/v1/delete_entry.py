"""Delete an entry in MyDiary"""
from flask import Flask, Request
from flask_restful import Resource, Api, reqparse

class DeleteEntry(Resource):
    def delete(self, entry_id):
        """Method to delete a diary entry"""
        entries = [1,2,3,4,5]
        entry = next(
            filter(lambda x: x['entry_id'] == entry_id, entries), None)
        if entry is None:
            return {'message': 'Item does not exist'}, 404
        else:
            entries.pop(entry['entry_id']-1)
            return {'message': 'Item deleted'}, 200
