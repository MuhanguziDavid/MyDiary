"""Update an entry in MyDiary"""
from flask import Flask
from flask_restful import Resource, Api, reqparse
import sys, os

sys.path.append(os.path.pardir)

from api.v1.data import entries


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

        entry = next(
            filter(lambda x: x['entry_id'] == entry_id, entries), None)
        if entry is None:
            return {'message': 'Item does not exist'}, 400
        else:
            entry.update(data)
            return entry, 200
