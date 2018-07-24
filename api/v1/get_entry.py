"""Get a specific entry in MyDiary"""
from flask import Flask
from flask_restful import Resource, Api, reqparse
import sys, os

sys.path.append(os.path.pardir)

from api.v1.data import entries

class GetEntry(Resource):
    """Class for GetEntry resource"""
    def get(self, entry_id):
        """method to get a specific diary entry"""
        entry = next(
            filter(lambda x: x['entry_id'] == entry_id, entries), None)
        return {'entry': entry}, 200 if entry else 404