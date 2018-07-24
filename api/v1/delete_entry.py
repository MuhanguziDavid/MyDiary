"""Delete an entry in MyDiary"""
from flask import Flask, Request
from flask_restful import Resource, Api, reqparse

from api.v1.data import entries

class DeleteEntry(Resource):
    def delete(self, entry_id):
        """Method to delete a diary entry"""
        entry = next(
            filter(lambda x: x['entry_id'] == entry_id, entries), None)
        if entry is None:
            return {'message': 'Item does not exist'}, 404
        else:
            entries.pop(entry['entry_id']-1)
            return {'message': 'Item deleted'}, 200
