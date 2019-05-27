# test_response_objects.py
import pytest

from book.response_objects import response_objects as res
from book.requests import book_list_request_objects as req


@pytest.fixture
def response_value():
    return {'key': ['value1', 'value2']}


@pytest.fixture
def response_type():
    return 'test response type'


@pytest.fixture
def response_message():
    return 'test error message'


def test_success_response_bools_to_true():
    assert bool(res.ResponseSuccess()) is True


def test_success_response_with_value_has_value(response_value):
    response = res.ResponseSuccess(response_value)
    assert response.value == response_value


def test_fail_response_bools_to_false(response_type, response_message):
    assert bool(res.ResponseFailure(response_type, response_message)) is False


def test_fail_with_type_and_msg_rtrns_params(response_type, response_message):
    response = res.ResponseFailure(response_type, response_message)
    assert response.type == response_type
    assert response.message == response_message


def test_fail_returns_value_as_dict(response_type, response_message):
    response = res.ResponseFailure(response_type, response_message)
    assert response.value == {'type': response_type, 'message':
                              response.message}


def test_fail_with_exception():
    response = res.ResponseFailure('type', Exception('generic exception'))
    assert response.type == 'type'
    assert response.message == 'Exception: generic exception'


def test_fail_response_with_invalid_request():
    request = req.InvalidRequest()
    request.add_error('param', 'error message')
    request.add_error('param2', 'error message2')

    result = res.ResponseFailure.build_response_from_invalid_request(request)

    expected_message = f'param: error message\nparam2: error message2'
    assert result.type == 'ParametersError'
    assert result.message == expected_message


def test_param_fail(response_message):
    response = res.ResponseFailure.build_parameter_failure(response_message)
    assert bool(response) is False
    assert response.type == res.ResponseFailure.PARAMETERS_ERROR
    assert response.message == response_message


def test_resourse_fail(response_message):
    response = res.ResponseFailure.build_resource_failure(response_message)
    assert bool(response) is False
    assert response.type == res.ResponseFailure.RESOURCE_ERROR
    assert response.message == response_message


def test_system_fail(response_message):
    response = res.ResponseFailure.build_system_failure(response_message)
    assert bool(response) is False
    assert response.type == res.ResponseFailure.SYSTEM_ERROR
    assert response.message == response_message
