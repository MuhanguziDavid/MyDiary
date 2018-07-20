"""Get all entries in MyDiary"""
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

entries = [
    {
        'entry_id': 1,
        'title': 'A day at the mall',
        'description': 'This day was spent at the mall'
    },
    {
        'entry_id': 2,
        'title': 'A sad day',
        'description': 'I was sad today'
    },
    {
        'entry_id': 3,
        'title': 'Happy hour',
        'description': 'Because I am happy'
    }
]


class Entry(Resource):
    """Class for Entry resource"""
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

    def get(self, entry_id):
        """method to get a specific diary entry"""
        entry = next(
            filter(lambda x: x['entry_id'] == entry_id, entries), None)
        return {'entry': entry}, 200 if entry else 404

    def post(self, entry_id):
        """Method to post a new diary entry"""
        if next(filter(lambda x: x['entry_id'] == entry_id, entries), None):
            return {'message': "Id '{}' exists.".format(entry_id)}, 400

        data = Entry.parser.parse_args()

        entry = {'entry_id': entry_id,
                 'title': data['title'], 'description': data['description']}
        entries.append(entry)
        return entry, 201


class EntryList(Resource):
    """Class for EntryList resource"""

    def get(self):
        """method to return all entries"""
        return {'entries': entries}


api.add_resource(Entry, '/entry/<int:entry_id>')
api.add_resource(EntryList, '/entries')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
