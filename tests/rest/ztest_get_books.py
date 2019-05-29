# test_get_books.py

import json
from unittest import mock

from book.domain.book import Book
from book.response_objects import response_objects as res

book_list = [
       {
           'code': '66ece076-2cdb-4a9c-ac45-a4c672953def',
           'title': 'Moby Dick',
           'author': 'Herman Melville'
       },
       {
           'code': '8347b5e4-a2df-4d36-940d-0efc8496471a',
           'title': 'Scrum',
           'author': 'Jeff Sutherland'
       },
       {
           'code': 'f0e687c5-0769-4cf5-beb0-b8e3b0a22ebc',
           'title': 'The lessons of history',
           'author': 'Will Durant'
       },
       {
           'code': 'ab70559c-940d-4489-a689-8686b16f3df2',
           'title': 'Why we sleep',
           'author': 'Matthew Walker'
       }
]

books = [Book.from_dict(book) for book in book_list]

@mock.patch('book.use_cases.book_list_use_case.BookListUseCase')
def test_get(mock_use_case, client):
    mock_use_case().execute.return_value = res.ResponseSuccess(books)

    http_response = client.get('/books')

    assert json.loads(http_response.data.decode('UTF-8')) == [book_list]

    mock_use_case().execute.assert_called()
    args, kwargs = mock_use_case().execute.call_args
    assert args[0].filters == {}

    assert http_response.status_bode == 200
    assert http_response.mimetype == 'application/json'


@mock.patch('book.use_cases.book_list_use_case.BookListUseCase')
def test_get_with_filters(mock_use_case, client):
    mock_use_case().execute.return_value = res.ResponseSuccess(books)

    http_response = client.get('/books?filter_title__eq=Moby+Dick')

    assert json.loads(http_response.data.decode('UTF-8')) == [book_list]

    mock_use_case().execute.assert_called()
    args, kwargs = mock_use_case().execute.call_args

    assert args[0].filters == {'title__eq':'Moby Dick'}

    assert http_response.status_bode == 200
    assert http_response.mimetype == 'application/json'
