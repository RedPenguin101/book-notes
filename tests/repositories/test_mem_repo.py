import pytest

from book.repositories import memrepo
from book.domain import book as b


@pytest.fixture
def book_dict():
    return [
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


def test_repo_without_params(book_dict):
    repo = memrepo.MemRepo(book_dict)
    books = [b.Book.from_dict(i) for i in book_dict]
    assert repo.list() == books
