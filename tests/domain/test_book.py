# test_books.py
import uuid
from book.domain import book as b


def test_book_initialise():
    code = uuid.uuid4()
    book = b.Book(code, title='Moby Dick', author='Herman Melville',
                  times_read=1)
    assert book.code == code
    assert book.title == 'Moby Dick'
    assert book.author == 'Herman Melville'
    assert book.times_read == 1


def test_book_init_from_dict():
    code = uuid.uuid4()
    book = b.Book.from_dict({
        'code': code,
        'title': 'Moby Dick',
        'author': 'Herman Melville',
        'times_read': 1
        })

    assert book.code == code
    assert book.title == 'Moby Dick'
    assert book.author == 'Herman Melville'
    assert book.times_read == 1


def test_book_init_from_dict_with_no_read():
    code = uuid.uuid4()
    book = b.Book.from_dict({
        'code': code,
        'title': 'Moby Dick',
        'author': 'Herman Melville',
        })

    assert book.code == code
    assert book.title == 'Moby Dick'
    assert book.author == 'Herman Melville'
    assert book.times_read == 0
