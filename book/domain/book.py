class Book:
    def __init__(self, code, title, author):
        self.title = title
        self.author = author
        self.code = code

    @classmethod
    def from_dict(cls, adict):
        return cls(adict['code'], adict['title'], adict['author'])

    def to_dict(self):
        return {
                'code': self.code,
                'title': self.title,
                'author': self.author
                }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()
