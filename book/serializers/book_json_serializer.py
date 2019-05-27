from json import JSONEncoder


class BookJsonEncoder(JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {
                    'code': str(o.code),
                    'title': o.title,
                    'author': o.author
                    }
            return to_serialize
        except AttributeError:
            return super().default(o)
