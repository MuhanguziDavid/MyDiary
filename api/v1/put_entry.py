"""Update an entry in MyDiary"""
from flask import Flask, Request
from flask_restful import Resource, Api, reqparse


class PutEntry(Resource):
    """Class for PutEntry resource"""
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

    def put(self, entry_id):
        """Method to modify an entry"""
        data = PutEntry.parser.parse_args()

        entries = [1,2,3,4,5]

        entry = next(
            filter(lambda x: x['entry_id'] == entry_id, entries), None)
        if entry is None:
            return {'message': 'Item does not exist'}, 404
        else:
            entry.update(data)
            return entry, 200
