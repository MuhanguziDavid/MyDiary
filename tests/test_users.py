"""Tests concerning users"""
import unittest
import json
import sys
from flask_jwt_extended import jwt_required, get_jwt_identity

from config import app
from tests import tests_data
from api.database.db import DatabaseConnection


class TestUsers(unittest.TestCase):
    """Different test cases for users"""

    def setUp(self):
        app.config['TESTING'] = True
        self.myapp = app.test_client()

        with app.app_context():
            database_connection = DatabaseConnection()
            database_connection.create_table_users()
            database_connection.create_table_entries()

    def test_signup_user_with_existing_name(self):
        """Test that a user will not be registered with a name that exists"""
        response = tests_data.registration(self, "grace", "mark@gmail.com", "1234", "1234") 

        self.assertEqual(response.status_code, 400)
        self.assertIn("username already exists", str(response.data))
    
    def test_signup_user_with_mismatching_passwords(self):
        """Test that a user will not be registered with mismatching passwords"""
        response = tests_data.registration(self, "grace", "mark@gmail.com", "1234", "5678")

        self.assertEqual(response.status_code, 400)
        self.assertIn("passwords dont match", str(response.data))

    def test_login_with_correct_credentials(self):
        """Test that a user will be logged in when credentials are right"""
        response = tests_data.login_user(self, "chris", "1234")

        self.assertEqual(response.status_code, 200)
        self.assertIn("Logged in Successfully", str(response.data))

    def test_login_with_wrong_username(self):
        """Test that a user will not be logged in with wrong username"""
        response = tests_data.login_user(self, "wrong", "1234")

        self.assertEqual(response.status_code, 401)
        self.assertIn(
            "Invalid username or password, please try again", str(response.data))

    def test_login_with_wrong_password(self):
        """Test that a user will not be logged in with wrong password"""
        response = tests_data.login_user(self, "chris", "wrong")

        self.assertEqual(response.status_code, 401)
        self.assertIn(
            "Password incorrect, please re-enter password", str(response.data))
    
    def tearDown(self):
        with app.app_context():
            pass

if __name__ == '__main__':
    unittest.main()
