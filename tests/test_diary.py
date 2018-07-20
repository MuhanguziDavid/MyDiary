"""Tests for get all entries"""
import unittest
import json
from api.v1 import diary


class TestDiaryEntries(unittest.TestCase):
    """Different test cases for Diary Entries"""

    def setUp(self):
        self.myapp = diary.app.test_client()

    def test_get_entries(self):
        """Test whether all diary entries are retreived"""
        response = self.myapp.get('/api/v1/entries')
        self.assertEqual(response.status_code, 200)

    def test_get_specific_entry(self):
        """Test whether a specific diary entry is retreived"""
        _id = {"entry_id": 1}
        response = self.myapp.get('/api/v1/entry/{}'.format(_id['entry_id']))
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

    def test_post_new_entry(self):
        """tests that a new entry will be created"""
        response = self.myapp.post('/api/v1/entry/5',
                                   data=json.dumps(dict(
                                       title='The year 1995',
                                       description='This is when I was born'
                                   )),
                                   content_type='application/json')

        self.assertEqual(response.status_code, 201)

    def test_post_with_existing_id(self):
        """tests that an entry wont be created if an existing entry_id is entered"""
        response = self.myapp.post('/api/v1/entry/3',
                                   data=json.dumps(dict(
                                       title='The year 1995',
                                       description='This is when I was born'
                                   )),
                                   content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_post_without_id(self):
        """tests that an entry wont be created without entering an id"""
        response = self.myapp.post('/api/v1/entry/',
                                   data=json.dumps(dict(
                                       title='The year 1995',
                                       description='This is when I was born'
                                   )),
                                   content_type='application/json')

        self.assertEqual(response.status_code, 404)

    def test_post_without_string_id(self):
        """tests that an entry wont be created if a string is entered as id"""
        response = self.myapp.post('/api/v1/entry/home',
                                   data=json.dumps(dict(
                                       title='The year 1995',
                                       description='This is when I was born'
                                   )),
                                   content_type='application/json')

        self.assertEqual(response.status_code, 404)

    def test_put_existing_entry(self):
        """tests that an entry will be updated"""
        response = self.myapp.put('/api/v1/entry/3',
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

        self.assertEqual(response.status_code, 200)

    def test_delete_entry(self):
        """Test whether a specific diary entry is deleted"""
        _id = {"entry_id": 2}
        response = self.myapp.delete('/api/v1/entry/{}'.format(_id['entry_id']))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Item deleted', str(response.data))


if __name__ == '__main__':
    unittest.main()