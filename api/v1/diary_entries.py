"""Get all entries in MyDiary"""
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

entries = [
    {
        'entry_id': '1',
        'title': 'A day at the mall',
        'description': 'This day was spent at the mall'
    },
    {
        'entry_id': '2',
        'title': 'A sad day',
        'description': 'I was sad today'
    },
    {
        'entry_id': '3',
        'title': 'Happy hour',
        'description': 'Because I am happy'
    }
]

class Entry(Resource):
    def get(self, name):
        entry = next(filter(lambda x: x['entry_id'] == name, entries), None)
        return {'entry': entry}, 200 if entry else 404


class EntryList(Resource):
    """EntryList class verrides Resource class"""
    def get(self):
        """method to return all entries"""
        return {'entries': entries}

api.add_resource(Entry, '/entry/<string:name>')
api.add_resource(EntryList, '/entries')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
