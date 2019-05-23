from book.requests import book_list_request_objects as req


def test_book_list_req_obj_init_no_filt():
    request = req.BookListRequest()
    assert request.filters is None
    assert bool(request) is True


def test_book_list_req_with_valid_filters():
    filters = {'filters': {
        'name__eq': 'Moby Dick',
        'author__eq': 'Herman Melville'
        }}

    request = req.BookListRequest.from_dict(filters)
    assert bool(request) is True
    assert request.filters == filters['filters']


def test_book_list_req_obj_fromdict_empty_filt():
    request = req.BookListRequest.from_dict({})
    assert bool(request) is True
    assert request.filters is None


def test_book_list_req_from_dict_with_filters_not_a_dict():
    request = req.BookListRequest.from_dict({'filters': 'not_a_dict'})
    assert bool(request) is False


def test_book_list_request_with_uncoded_filter_returns_invalid():
    filters = {'filters': {'fake_filter': 10}}
    request = req.BookListRequest.from_dict(filters)
    assert bool(request) is False
