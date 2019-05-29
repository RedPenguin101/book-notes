from book.domain import book as b


class MemRepo:
    def __init__(self, book_dict):
        self.books = [b.Book.from_dict(i) for i in book_dict]

    def list(self, filters=None):
        if not filters:
            return self.books

        results = self.books.copy()

        if 'title__eq' in filters:
            temp = []

            for book in results:
                if filters['title__eq'] == book.title:
                    temp.append(book)

            results = temp

        if 'author__eq' in filters:
            temp = []

            for book in results:
                if filters['author__eq'] == book.author:
                    temp.append(book)
            results = temp

        return results
