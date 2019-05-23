import json
import uuid

from book.domain import book as b
from book.serializers import book_json_serializer as ser


def test_serialize_book_rule():
    code = uuid.uuid4()
    book = b.Book(code, title='Moby Dick', author='Herman Melville')

    json_output = json.dumps(book, cls=ser.BookJsonEncoder)
    expected_json = ("""{"code": "%s", "title": "Moby Dick", "author":"""
                     """ "Herman Melville"}""") % (code)
    assert json_output == expected_json
