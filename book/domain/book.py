# book.py
class Book:
    def __init__(self, code, title, author, times_read=0):
        self.title = title
        self.author = author
        self.code = code
        self.times_read = times_read

    @classmethod
    def from_dict(cls, adict):
        return cls(adict['code'], adict['title'], adict['author'],
                   adict.get('times_read', 0))

    def to_dict(self):
        return {
                'code': self.code,
                'title': self.title,
                'author': self.author
                }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()
