from flask import Flask, Request
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import JWTManager

app = Flask(__name__)

secret_key = 'david'
app.config['JWT_SECRET_KEY'] = secret_key
jwt = JWTManager(app)

app.config['TESTING'] == False
app.config['DEBUG'] = True

app.config['TEST_DATABASE'] = "test_diary"
app.config['DATABASE'] = "mydiary"
app.config.from_object(__name__)
