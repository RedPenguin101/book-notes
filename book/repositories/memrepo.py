from book.domain import book as b


class MemRepo:
    def __init__(self, book_dict):
        self.books = [b.Book.from_dict(i) for i in book_dict]

    def list(self):
        return self.books
