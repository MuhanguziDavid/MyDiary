"""Tests concerning diary entries"""
import unittest
import json
import sys
from flask_jwt_extended import jwt_required, get_jwt_identity

from api.database.db import DatabaseConnection
from api import app
from tests import tests_data


class TestDiaryEntries(unittest.TestCase):
    """Different test cases for Diary Entries"""

    def setUp(self):
        app.config['TESTING'] = True
        self.myapp = app.test_client()

        with app.app_context():
            database_connection = DatabaseConnection()
            database_connection.create_table_users()
            database_connection.create_table_entries()
    
    def test_signup_user(self):
        """Test that a user will be registered"""
        response = tests_data.registration(self, "david", "david@gmail.com", "1234", "1234") 

        self.assertEqual(response.status_code, 201)
        self.assertIn("Account Created Successfully", str(response.data))

    
    def test_signup_user_with_existing_name(self):
        """Test that a user will not be registered with a name that exists"""
        tests_data.registration(self, "david", "david@gmail.com", "1234", "1234")
        response = tests_data.registration(self, "david", "david@gmail.com", "1234", "1234") 

        self.assertEqual(response.status_code, 400)
        self.assertIn("username already exists", str(response.data))
    
    def test_signup_user_with_mismatching_passwords(self):
        """Test that a user will not be registered with mismatching passwords"""
        response = tests_data.registration(self, "grace", "mark@gmail.com", "1234", "5678")

        self.assertEqual(response.status_code, 400)
        self.assertIn("passwords dont match", str(response.data))

    def test_login_with_correct_credentials(self):
        """Test that a user will be logged in when credentials are right"""
        tests_data.registration(self, "chris", "chris@gmail.com", "1234", "1234")
        response = tests_data.login_user(self, "chris", "1234")

        self.assertEqual(response.status_code, 200)
        self.assertIn("Logged in Successfully", str(response.data))

    def test_login_with_wrong_username(self):
        """Test that a user will not be logged in with wrong username"""
        tests_data.registration(self, "chris", "chris@gmail.com", "1234", "1234")
        response = tests_data.login_user(self, "wrong", "1234")

        self.assertEqual(response.status_code, 401)
        self.assertIn(
            "Invalid username or password, please try again", str(response.data))

    def test_login_with_wrong_password(self):
        """Test that a user will not be logged in with wrong password"""
        tests_data.registration(self, "chris", "chris@gmail.com", "1234", "1234")
        response = tests_data.login_user(self, "chris", "wrong")

        self.assertEqual(response.status_code, 401)
        self.assertIn(
            "Password incorrect, please re-enter password", str(response.data))
    
    def test_post_entry(self):
        """tests that a new entry will not be created if the same title is given"""
        # login user
        tests_data.registration(self, "chris", "chris@gmail.com", "1234", "1234")
        login = tests_data.login_user(self, "chris", "1234")
        user_login_data = json.loads(login.data.decode())

        # post data after being authenticated
        response = tests_data.post_data(self, user_login_data, "Test post")

        self.assertIn("Entry has been created", str(response.data))
        self.assertEqual(response.status_code, 201)
    
    def test_post_with_existing_title(self):
        """tests that a new entry will not be created if the same title is given"""
        # login user
        tests_data.registration(self, "chris", "chris@gmail.com", "1234", "1234")
        login = tests_data.login_user(self, "chris", "1234")
        user_login_data = json.loads(login.data.decode())

        # post data after being authenticated
        tests_data.post_data(self, user_login_data, "Test post")
        response = tests_data.post_data(self, user_login_data, "Test post")

        self.assertIn(
            "An entry with the same title exists, please try again", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_get_entries(self):
        """Test whether all diary entries are retreived"""
        # first login user chris
        tests_data.registration(self, "chris", "chris@gmail.com", "1234", "1234")
        login = tests_data.login_user(self, "chris", "1234")
        user_login_data = json.loads(login.data.decode())

        #post entries
        tests_data.post_data(self, user_login_data, "Test post")
        tests_data.post_data(self, user_login_data, "second Test post")

        # get entries for user chris
        response = tests_data.get_all_records(self, user_login_data)
        self.assertEqual(response.status_code, 200)

    def test_get_specific_entry(self):
        """Test whether a specific diary entry is retreived"""
        # login user chris
        tests_data.registration(self, "chris", "chris@gmail.com", "1234", "1234")
        login = tests_data.login_user(self, "chris", "1234")
        user_login_data = json.loads(login.data.decode())

        #post entries
        tests_data.post_data(self, user_login_data, "Test post")
        tests_data.post_data(self, user_login_data, "second Test post")

        # get entry
        response = tests_data.get_specific_record(self, user_login_data, 1)
        self.assertEqual(response.status_code, 200)

    def test_get_non_existing_entry(self):
        """
        tests whether it will returen status code 404 (not found)
        if a user tries to retreive non existing entry
        """
        # login user
        tests_data.registration(self, "chris", "chris@gmail.com", "1234", "1234")
        login = tests_data.login_user(self, "chris", "1234")
        user_login_data = json.loads(login.data.decode())

        #post entries
        tests_data.post_data(self, user_login_data, "Test post")

        # get entry
        response = tests_data.get_specific_record(self, user_login_data, 11)
        self.assertIn("Entry was not found", str(response.data))
        self.assertEqual(response.status_code, 404)

    def test_get_entry_with_missing_key(self):
        """Tests that the api will not get an entry with out id"""
        # login user
        tests_data.registration(self, "chris", "chris@gmail.com", "1234", "1234")
        login = tests_data.login_user(self, "chris", "1234")
        user_login_data = json.loads(login.data.decode())

        #post entries
        tests_data.post_data(self, user_login_data, "Test post")

        _id = {"entry_id": None}
        response = self.myapp.get('/api/v1/entry/{}'.format(_id['entry_id']))
        self.assertEqual(response.status_code, 404)

    def test_get_entry_with_non_integer_key(self):
        """Tests that the api will not get an entry with non integer key"""
        # login user
        tests_data.registration(self, "chris", "chris@gmail.com", "1234", "1234")
        login = tests_data.login_user(self, "chris", "1234")
        user_login_data = json.loads(login.data.decode())

        #post entries
        tests_data.post_data(self, user_login_data, "Test post")

        _id = {"entry_id": 'home'}
        response = self.myapp.get('/api/v1/entry/{}'.format(_id['entry_id']))
        self.assertEqual(response.status_code, 404)

    

    def test_update_entry_less_than_24hrs(self):
        """tests that an entry will not be updated if it was created over 24 hours ago"""
        # login user chris
        tests_data.registration(self, "chris", "chris@gmail.com", "1234", "1234")
        login = tests_data.login_user(self, "chris", "1234")
        user_login_data = json.loads(login.data.decode())

        #post entries
        tests_data.post_data(self, user_login_data, "Test post")

        # edit a record in chris' diary
        response = tests_data.put_data(self, user_login_data, 1)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Entry has been updated successfully", str(response.data))

    def test_delete_entry(self):
        """Test whether a specific diary entry is deleted"""
        # login user chris
        tests_data.registration(self, "chris", "chris@gmail.com", "1234", "1234")
        login = tests_data.login_user(self, "chris", "1234")
        user_login_data = json.loads(login.data.decode())

        #post entries
        tests_data.post_data(self, user_login_data, "Test post")

        # delete the posted record
        response = tests_data.delete_data(self, user_login_data, 1)
        self.assertEqual(response.status_code, 200)
        self.assertIn('The entry has been deleted', str(response.data))
    
    def test_delete_entry_that_does_not_exist(self):
        """Test whether a specific diary entry is deleted"""
        # login user chris
        tests_data.registration(self, "chris", "chris@gmail.com", "1234", "1234")
        login = tests_data.login_user(self, "chris", "1234")
        user_login_data = json.loads(login.data.decode())

        #post entries
        tests_data.post_data(self, user_login_data, "Test post")

        # delete the posted record
        response = tests_data.delete_data(self, user_login_data, 3)
        self.assertEqual(response.status_code, 400)
        self.assertIn('The entry with id {} does not exist'.format(3), str(response.data))
    
    def tearDown(self):
        with app.app_context():
            database_connection = DatabaseConnection()
            database_connection.drop_table_users()
            database_connection.drop_table_entries()


if __name__ == '__main__':
    unittest.main()
