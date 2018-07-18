"""Tests for get all entries"""
import unittest
import json
from api.v1 import diary_entries


class TestDiaryEntries(unittest.TestCase):
    """Different test cases for Diary Entries"""

    def setUp(self):
        self.myapp = diary_entries.app.test_client()

    def test_get_entries(self):
        """Test whether all diary entries are retreived"""
        response = self.myapp.get('/entries')
        self.assertEqual(response.status_code, 200)

    def test_get_specific_entry(self):
        """Test whether a specific diary entry is retreived"""
        _id = {"entry_id": 1}
        response = self.myapp.get('/entry/{}'.format(_id['entry_id']))
        self.assertEqual(response.status_code, 200)

    def test_get_non_existing_entry(self):
        """tests whether it will returen status code 404 (not found)"""
        _id = {"entry_id": 9}
        response = self.myapp.get('/entry/{}'.format(_id['entry_id']))
        self.assertEqual(response.status_code, 404)

    def test_post_new_entry(self):
        """tests whether it will returen status code 201 (created)"""
        response = self.myapp.post('/entry/5',
                                   data=json.dumps(dict(
                                       title='The year 1995',
                                       description='This is when I was born'
                                   )),
                                   content_type='application/json')

        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
