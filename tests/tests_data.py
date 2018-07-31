"""Tests concerning diary entries"""
import json

def registration(self, username, email, password, confirm_password):
    """Data to be use for create user endpoint tests"""
    response = self.myapp.post(
        '/api/v1/auth/signup',
        data=json.dumps(dict(username=username, email=email,
                             password=password, confirm_password=confirm_password)),
        content_type='application/json')
    return response


def login_user(self, username, password):
    """Data to be used for loging user in tests"""
    response = self.myapp.post(
        '/api/v1/auth/login',
        data=json.dumps(dict(username=username, password=password)),
        content_type='application/json')
    return response


def post_data(self, user_login_data, post_title):
    """Data to be used by the post endpoint tests"""
    response = self.myapp.post(
        '/api/v1/add',
        headers=dict(Authorization='Bearer '+user_login_data["auth_token"]),
        data=json.dumps(
            dict(title="", description="This is test data")),
        content_type='application/json')
    return response


def get_all_records(self, user_login_data):
    """Data to be used by the get entries endpoint"""
    response = self.myapp.get(
        '/api/v1/entries',
        headers=dict(Authorization='Bearer '+user_login_data["auth_token"]))
    return response


def get_specific_record(self, user_login_data, entry_id):
    """Data to be used by the get an entry endpoint tests"""
    response = self.myapp.get(
        '/api/v1/entry/{}'.format(entry_id),
        headers=dict(Authorization='Bearer '+user_login_data["auth_token"]))
    return response


def put_data(self, user_login_data, entry_id):
    """Data to be used by the put endpoint tests"""
    response = self.myapp.put(
        '/api/v1/update',
        headers=dict(Authorization='Bearer '+user_login_data["auth_token"]),
        data=json.dumps(dict(entry_id=entry_id, title='Last week',
                             description='I started practicing flask')),
        content_type='application/json')
    return response


def delete_data(self, user_login_data, entry_id):
    """Data to be used by the delete entrypoint tests"""
    response = self.myapp.delete(
        '/api/v1/remove',
        headers=dict(Authorization='Bearer ' +
                     user_login_data["auth_token"]),
        data=json.dumps(dict(entry_id=entry_id)),
        content_type='application/json')
    return response
