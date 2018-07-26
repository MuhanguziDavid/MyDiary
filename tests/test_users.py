"""Tests concerning users"""
import unittest
import json
import sys
import os

sys.path.append(os.path.pardir)

from api import app


class TestUsers(unittest.TestCase):
    """Different test cases for users"""

    def setUp(self):
        self.myapp = app.test_client()

    def test_signup_user_with_existing_name(self):
        """Test that a user will not be registered with a name that exists"""
        response = self.myapp.post('/api/v1/auth/signup',
                                   data=json.dumps(dict(
                                       name="grace",
                                       email="mark@gmail.com",
                                       password="1234",
                                       confirm_password="1234"
                                   )),
                                   content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertIn("username already exists", str(response.data))

    def test_login_with_correct_credentials(self):
        """Test that a user will be logged in when credentials are right"""
        response = self.myapp.post('/api/v1/auth/login',
                                   data=json.dumps(dict(
                                       name="chris",
                                       password="1234",
                                   )),
                                   content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertIn("Logged in Successfully", str(response.data))

    def test_login_with_wrong_username(self):
        """Test that a user will not be logged in with wrong username"""
        response = self.myapp.post('/api/v1/auth/login',
                                   data=json.dumps(dict(
                                       name="wrong",
                                       password="1234",
                                   )),
                                   content_type='application/json')

        self.assertEqual(response.status_code, 401)
        self.assertIn(
            "Invalid username or password, please try again", str(response.data))

    def test_login_with_wrong_password(self):
        """Test that a user will not be logged in with wrong password"""
        response = self.myapp.post('/api/v1/auth/login',
                                   data=json.dumps(dict(
                                       name="chris",
                                       password="wrong",
                                   )),
                                   content_type='application/json')

        self.assertEqual(response.status_code, 401)
        self.assertIn(
            "Password incorrect, please re-enter password", str(response.data))
