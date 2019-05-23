import pytest
import uuid
from unittest import mock

from book.domain import book as b
from book.use_cases import book_list_use_case as uc


@pytest.fixture
def books():
    b1 = b.Book(uuid.uuid4(), 'Moby Dick', 'Herman Melville')
    b2 = b.Book(uuid.uuid4(), 'Scrum', 'Jeff Sutherland')
    b3 = b.Book(uuid.uuid4(), 'The Lessons of History', 'Will Durant')
    b4 = b.Book(uuid.uuid4(), 'Why we sleep', 'Matthew Walker')

    return [b1, b2, b3, b4]


def test_book_list_uc_initiates(books):
    mock_repo = mock.Mock()
    mock_repo.list.return_value = books

    use_case = uc.BookListUseCase(mock_repo)
    assert use_case.repo == mock_repo


def test_book_list_uc_executes_with_empty_request(books):
    mock_repo = mock.Mock()
    mock_repo.list.return_value = books

    use_case = uc.BookListUseCase(mock_repo)
    response = use_case.execute(None)

    assert response == books
