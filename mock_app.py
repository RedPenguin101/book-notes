# mock_app.py

import requests

URL = 'http://127.0.0.1:5000/'


def get_book_list(title=None, author=None):
    url = URL + 'books'
    filters = {}

    if title:
        filters['title__eq'] = title
    if author:
        filters['author__eq'] = author

    if not filters:
        return requests.get(url=url).json()

    return requests.get(url=url, params=filters).json()
