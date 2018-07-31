"""Tests concerning diary entries"""
import unittest
import json
import sys
from flask_jwt_extended import jwt_required, get_jwt_identity

from api import app
from tests import tests_data


class TestDiaryEntries(unittest.TestCase):
    """Different test cases for Diary Entries"""

    def setUp(self):
        app.config['TEST_MODE'] = True
        self.myapp = app.test_client()

    def test_get_entries(self):
        """Test whether all diary entries are retreived"""
        # first login user chris
        login = tests_data.login_user(self, "chris", "1234")
        user_login_data = json.loads(login.data.decode())

        # get entries for user chris
        response = tests_data.get_all_records(self, user_login_data)
        self.assertEqual(response.status_code, 200)

    def test_get_specific_entry(self):
        """Test whether a specific diary entry is retreived"""
        # login user chris
        login = tests_data.login_user(self, "chris", "1234")
        user_login_data = json.loads(login.data.decode())

        # get entry with id 29 from david's diary
        response = tests_data.get_specific_record(self, user_login_data, 8)
        self.assertEqual(response.status_code, 200)

    def test_get_non_existing_entry(self):
        """
        tests whether it will returen status code 404 (not found)
        if a user tries to retreive non existing entry
        """
        # login user
        login = tests_data.login_user(self, "chris", "1234")
        user_login_data = json.loads(login.data.decode())

        # get entry with id 29 from david's diary
        response = tests_data.get_specific_record(self, user_login_data, 11)
        self.assertIn("Entry was not found", str(response.data))
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
        # login user
        login = tests_data.login_user(self, "chris", "1234")
        user_login_data = json.loads(login.data.decode())

        # post data after being authenticated
        response = tests_data.post_data(self, user_login_data, "Test post")

        self.assertIn(
            "An entry with the same title exists, please try again", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_post_without_title(self):
        """tests that a new entry will not be created title is not given"""
        # login user
        login = tests_data.login_user(self, "chris", "1234")
        user_login_data = json.loads(login.data.decode())

        # post data after being authenticated
        response = tests_data.post_data(self, user_login_data, None)

        self.assertEqual(response.status_code, 500)
        self.assertIn("Internal Server Error", str(response.data))

    def test_update_entry_more_than_24hrs(self):
        """tests that an entry will not be updated if it was created over 24 hours ago"""
        # login user chris
        login = tests_data.login_user(self, "chris", "1234")
        user_login_data = json.loads(login.data.decode())

        # edit a record in chris' diary
        response = tests_data.put_data(self, user_login_data, 9)

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "Entry can not be updated, it was created over 24 hours ago", str(response.data))

    def test_delete_entry(self):
        """Test whether a specific diary entry is deleted"""
        # login user chris
        login = tests_data.login_user(self, "chris", "1234")
        user_login_data = json.loads(login.data.decode())

        # delete the posted record
        response = tests_data.delete_data(self, user_login_data, 13)
        self.assertEqual(response.status_code, 200)
        self.assertIn('The entry has been deleted', str(response.data))


if __name__ == '__main__':
    unittest.main()
