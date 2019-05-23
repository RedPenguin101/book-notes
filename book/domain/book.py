class Book:
    def __init__(self, code, title, author):
        self.title = title
        self.author = author
        self.code = code

    @classmethod
    def from_dict(cls, adict):
        return cls(adict['code'], adict['title'], adict['author'])
