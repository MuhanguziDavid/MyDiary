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
        """tests whether it will returen status code 404 (not found)
        if a user tries to retreive non existing entry
        """
        _id = {"entry_id": 9}
        response = self.myapp.get('/entry/{}'.format(_id['entry_id']))
        self.assertEqual(response.status_code, 404)

    def test_post_new_entry(self):
        """tests whether new entry will be created"""
        response = self.myapp.post('/entry/5',
                                   data=json.dumps(dict(
                                       title='The year 1995',
                                       description='This is when I was born'
                                   )),
                                   content_type='application/json')

        self.assertEqual(response.status_code, 201)

    def test_post_with_existing_id(self):
        """tests whether it will returen status code 400 (bad request)
        if an existing entry_id is entered
        """
        response = self.myapp.post('/entry/3',
                                   data=json.dumps(dict(
                                       title='The year 1995',
                                       description='This is when I was born'
                                   )),
                                   content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_put_existing_entry(self):
        """tests whether an entry will be updates
        returns status code 200 (okay)
        """
        response = self.myapp.put('/entry/3',
                                  data=json.dumps(dict(
                                      title='This week',
                                      description='I started practicing flask'
                                  )),
                                  content_type='application/json')

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
