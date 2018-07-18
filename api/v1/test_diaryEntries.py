"""Tests for get all entries"""
import unittest
import diary_entries

class TestDiaryEntries(unittest.TestCase):
    def setUp(self):
        self.myapp = diary_entries.app.test_client()

    def test_get_entries(self):
        """Test whether all diary entries are retreived"""
        response = self.myapp.get('/entries')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()