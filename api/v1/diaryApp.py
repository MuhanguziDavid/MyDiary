"""Api enpoint logic"""
from flask import Flask
from flask_restful import Resource, Api, reqparse

from get_entries import EntryList
from get_entry import GetEntry
from post_entry import PostEntry
from put_entry import PutEntry
from delete_entry import DeleteEntry

app = Flask(__name__)
api = Api(app)

api.add_resource(EntryList, '/api/v1/entries') #get all diary entries
api.add_resource(GetEntry, '/api/v1/entry/<int:entry_id>') #get specific diary entry
api.add_resource(PostEntry, '/api/v1/entry/<int:entry_id>') #add a diary entry
api.add_resource(PutEntry, '/api/v1/entry/<int:entry_id>') #update a diary entry
api.add_resource(DeleteEntry, '/api/v1/entry/<int:entry_id>') #update a diary entry

if __name__ == '__main__':
    app.run(port=5000, debug=True)
