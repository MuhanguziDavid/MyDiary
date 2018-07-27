"""Get all entries in MyDiary"""
from flask import Flask, Request
from flask_restful import Resource, Api, reqparse

from api.v1.data import entries


class EntryList(Resource):
    """Class for EntryList resource"""

    def get(self):
        """method to return all entries"""
        return {'entries': entries}, 200
