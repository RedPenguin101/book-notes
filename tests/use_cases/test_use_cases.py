import pytest
import uuid
from unittest import mock

from book.domain import book as b
from book.use_cases import book_list_use_case as uc
from book.requests import book_list_request_objects as req
from book.response_objects import response_objects as res


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

    request = req.BookListRequest()
    response = use_case.execute(request)

    assert response.value == books
    assert bool(response) is True
    mock_repo.list.assert_called_with(filters=None)


def test_book_list_uc_bools_to_false_with_invalid_req(books):
    mock_repo = mock.Mock()
    mock_repo.list.return_value = books

    use_case = uc.BookListUseCase(mock_repo)
    filters = {'bad_request': 'Moby Dick'}
    request = req.BookListRequest.from_dict({'filters': filters})

    response = use_case.execute(request)

    assert bool(request) is False
    assert bool(response) is False


def test_request_with_valid_params_calls_repo_with_filt(books):
    mock_repo = mock.Mock()
    mock_repo.list.return_value = books

    use_case = uc.BookListUseCase(mock_repo)
    filters = {'title__eq': 'Moby Dick'}
    request = req.BookListRequest.from_dict({'filters': filters})

    response = use_case.execute(request)

    assert bool(response) is True
    mock_repo.list.assert_called_with(filters=filters)


def test_use_case_catches_generic_error(books):
    mock_repo = mock.Mock()
    mock_repo.list.side_effect = Exception('generic exception')

    use_case = uc.BookListUseCase(mock_repo)

    filters = {'title__eq': 'Moby Dick'}
    request = req.BookListRequest.from_dict({'filters': filters})

    response = use_case.execute(request)

    assert bool(response) is False
    assert response.type == res.ResponseFailure.SYSTEM_ERROR
    assert response.message == 'Exception: generic exception'
