"""Post an entry to MyDiary"""
from flask import Flask
from flask_restful import Resource, Api, reqparse

from data import entries

class PostEntry(Resource):
    """Class for PostEntry resource"""
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

    def post(self, entry_id):
        """Method to post a new diary entry"""
        if next(filter(lambda x: x['entry_id'] == entry_id, entries), None):
            return {'message': "An item with name '{}' already exists.".format(entry_id)}, 400

        data = PostEntry.parser.parse_args()

        entry = {'entry_id': entry_id,
                 'title': data['title'],
                 'description': data['description']}
        entries.append(entry)
        return entry, 201