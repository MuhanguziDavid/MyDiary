"""Get all entries in MyDiary"""
from flask import Flask
from flask_restful import Resource, Api, reqparse
import sys, os

sys.path.append(os.path.pardir)

from api.v1.data import entries

class EntryList(Resource):
    """Class for EntryList resource"""

    def get(self):
        """method to return all entries"""
        return {'entries': entries}
