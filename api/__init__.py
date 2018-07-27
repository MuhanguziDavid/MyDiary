"""Api enpoint logic"""
from flask import Flask, Request
from flask_restful import Resource, Api, reqparse

from api.v1.get_entries import EntryList
from api.v1.get_entry import GetEntry
from api.v1.post_entry import PostEntry
from api.v1.put_entry import PutEntry
from api.v1.delete_entry import DeleteEntry

app = Flask(__name__)
api = Api(app)

# get all diary entries
api.add_resource(EntryList, '/api/v1/entries')
# get specific diary entry
api.add_resource(GetEntry, '/api/v1/entry/<int:entry_id>')
# add a diary entry
api.add_resource(PostEntry, '/api/v1/entry/<int:entry_id>')
# update a diary entry
api.add_resource(PutEntry, '/api/v1/entry/<int:entry_id>')
# delete a diary entry
api.add_resource(DeleteEntry, '/api/v1/entry/<int:entry_id>')
