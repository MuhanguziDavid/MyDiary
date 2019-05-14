"""Api enpoint logic"""
from flask import Flask, Request
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import JWTManager
from flask_cors import CORS, cross_origin

from api.database.db import DatabaseConnection
from api.v1.get_entries import EntryList
from api.v1.get_entry import GetEntry
from api.v1.post_entry import PostEntry
from api.v1.put_entry import PutEntry
from api.v1.delete_entry import DeleteEntry
from api.v1.create_user import CreateUser
from api.v1.login import Log_In

app = Flask(__name__)
api = Api(app)
CORS(app)

secret_key = 'david'
app.config['JWT_SECRET_KEY'] = secret_key
jwt = JWTManager(app)

api.add_resource(EntryList, '/api/v1/entries')  # get all diary entries
api.add_resource(GetEntry, '/api/v1/entries/<int:entry_id>')  # get an entry
api.add_resource(PostEntry, '/api/v1/entries')  # add a diary entry
api.add_resource(PutEntry, '/api/v1/entries/<int:entry_id>')  # update an entry
api.add_resource(DeleteEntry, '/api/v1/entries/<int:entry_id>')  # update entry
api.add_resource(CreateUser, '/api/v1/auth/signup')  # register a user
api.add_resource(Log_In, '/api/v1/auth/login')  # login a user
