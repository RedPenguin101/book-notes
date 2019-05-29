# rest/book.py
import json

from flask import Blueprint, Response, request

from book.repositories import memrepo as mr
from book.use_cases import book_list_use_case as uc
from book.serializers import book_json_serializer as ser
from book.requests import book_list_request_objects as req
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

blueprint = Blueprint('book', __name__)

STATUS_CODES = {
        res.ResponseSuccess.SUCCESS: 200,
        res.ResponseFailure.RESOURCE_ERROR: 404,
        res.ResponseFailure.PARAMETERS_ERROR: 400,
        res.ResponseFailure.SYSTEM_ERROR: 500,
        }

@blueprint.route('/books', methods=['GET'])
def book():
    query_string = {'filters': {}}

    for arg, values in request.args.items():
        if arg.startswith('filter_'):
            query_string['filters'][arg.replace('filter_','')] = values

    request_object = req.BookListRequest.from_dict(query_string)

    repo = mr.MemRepo(book_list)
    use_case = uc.BookListUseCase(repo)
    response_object = use_case.execute(request_object)

    return Response(json.dumps(response_object.value, cls=ser.BookJsonEncoder),
            mimetype='application/json',
            status=STATUS_CODES[response_object.type])
