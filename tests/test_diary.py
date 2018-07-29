"""Tests concerning diary entries"""
import unittest
import json
import sys
from flask_jwt_extended import jwt_required, get_jwt_identity

from api import app


class TestDiaryEntries(unittest.TestCase):
    """Different test cases for Diary Entries"""

    def setUp(self):
        self.myapp = app.test_client()

    def test_get_entries(self):
        """Test whether all diary entries are retreived"""
        # first login user chris
        response = self.myapp.post('/api/v1/auth/login',
                                   data=json.dumps(dict(
                                       username="chris",
                                       password="1234",
                                   )),
                                   content_type='application/json')
        user_login_data = json.loads(response.data.decode())

        # get entries for user chris
        response = self.myapp.get('/api/v1/entries',
                                  headers=dict(Authorization='Bearer '+user_login_data["auth_token"]))
        self.assertEqual(response.status_code, 200)

    def test_get_specific_entry(self):
        """Test whether a specific diary entry is retreived"""
        self.myapp.post('/api/v1/entry/1',
                        data=json.dumps(dict(
                            title='The year 1995',
                            description='This is when I was born'
                        )),
                        content_type='application/json')
        response = self.myapp.get('/api/v1/entry/{}'.format(1))
        self.assertEqual(response.status_code, 200)

    def test_get_non_existing_entry(self):
        """tests whether it will returen status code 404 (not found)
        if a user tries to retreive non existing entry
        """
        _id = {"entry_id": 9}
        response = self.myapp.get('/api/v1/entry/{}'.format(_id['entry_id']))
        self.assertEqual(response.status_code, 404)

    def test_get_entry_with_missing_key(self):
        """Tests that the api will not get an entry with out id"""
        _id = {"entry_id": None}
        response = self.myapp.get('/api/v1/entry/{}'.format(_id['entry_id']))
        self.assertEqual(response.status_code, 404)

    def test_get_entry_with_non_integer_key(self):
        """Tests that the api will not get an entry with non integer key"""
        _id = {"entry_id": 'home'}
        response = self.myapp.get('/api/v1/entry/{}'.format(_id['entry_id']))
        self.assertEqual(response.status_code, 404)

    def test_post_with_existing_title(self):
        """tests that a new entry will not be created if the same title is given"""
        # login use chris and get token
        login = self.myapp.post('/api/v1/auth/login',
                                   data=json.dumps(dict(
                                       username="chris",
                                       password="1234",
                                   )),
                                   content_type='application/json')
        user_login_data = json.loads(login.data.decode())

        # post data after being authenticated
        response = self.myapp.post('/api/v1/add',
                                   headers=dict(
                                       Authorization='Bearer '+user_login_data["auth_token"]),
                                   data=json.dumps(dict(
                                       title="The year 1995",
                                       description="This is when I was born"
                                   )),
                                   content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertIn("An entry with the same title exists, please try again", str(response.data))

    def test_post_without_title(self):
        """tests that a new entry will not be created title is not given"""
        # login use chris and get token
        login = self.myapp.post('/api/v1/auth/login',
                                   data=json.dumps(dict(
                                       username="chris",
                                       password="1234",
                                   )),
                                   content_type='application/json')
        user_login_data = json.loads(login.data.decode())

        # post data after being authenticated
        response = self.myapp.post('/api/v1/add',
                                   headers=dict(
                                       Authorization='Bearer '+user_login_data["auth_token"]),
                                   data=json.dumps(dict(
                                       title=None,
                                       description="This is when I was born"
                                   )),
                                   content_type='application/json')

        self.assertEqual(response.status_code, 500)
        self.assertIn("Internal Server Error", str(response.data))

    def test_put_existing_entry(self):
        """tests that an entry will be updated"""
        self.myapp.post('/api/v1/entry/1',
                        data=json.dumps(dict(
                            title='The year 1995',
                            description='This is when I was born'
                        )),
                        content_type='application/json')
        response = self.myapp.put('/api/v1/entry/1',
                                  data=json.dumps(dict(
                                      title='This week',
                                      description='I started practicing flask'
                                  )),
                                  content_type='application/json')

        self.assertEqual(response.status_code, 200)

    def test_put_with_new_id(self):
        """tests that a new entry will be created if a new id is used"""
        response = self.myapp.put('/api/v1/entry/6',
                                  data=json.dumps(dict(
                                      title='This week',
                                      description='I started practicing flask'
                                  )),
                                  content_type='application/json')

        self.assertEqual(response.status_code, 404)

    def test_delete_entry(self):
        """Test whether a specific diary entry is deleted"""
        self.myapp.post('/api/v1/entry/1',
                        data=json.dumps(dict(
                            title='The year 1995',
                            description='This is when I was born'
                        )),
                        content_type='application/json')
        response = self.myapp.delete(
            '/api/v1/entry/{}'.format(1))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Item deleted', str(response.data))


if __name__ == '__main__':
    unittest.main()
