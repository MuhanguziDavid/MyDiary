"""Dummy data for the api"""
import sys, os

sys.path.append(os.path.pardir)
# list with data to be converted to JSONdictionary
entries = [
    {
        'entry_id': 1,
        'title': 'A day at the mall',
        'description': 'This day was spent at the mall'
    },
    {
        'entry_id': 2,
        'title': 'A sad day',
        'description': 'I was sad today'
    },
    {
        'entry_id': 3,
        'title': 'Happy hour',
        'description': 'Because I am happy'
    }
]