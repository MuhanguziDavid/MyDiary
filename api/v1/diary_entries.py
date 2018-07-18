from flask import Flask, request
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

class EntryList(Resource):
    def get(self):
        return {'entries': entries}

api.add_resource(EntryList, '/entries')

app.run(port=5000, debug=True)
