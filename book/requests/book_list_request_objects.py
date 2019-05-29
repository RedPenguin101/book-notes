class InvalidRequest:
    def __init__(self):
        self.errors = []

    def add_error(self, parameter, message):
        self.errors.append({'parameter': parameter, 'message': message})

    def has_errors(self):
        return len(self.errors) > 0

    def __bool__(self):
        return False


class ValidRequest:
    def __bool__(self):
        return True


class BookListRequest(ValidRequest):
    accepted_filters = ['title__eq', 'author__eq']

    def __init__(self, filters=None):
        self.filters = filters

    @classmethod
    def from_dict(cls, adict):

        invalid_req = InvalidRequest()

        if 'filters' in adict:
            if not isinstance(adict['filters'], dict):
                invalid_req.add_error('filters', 'Is not a dictionary')
                return invalid_req

            for key, value in adict['filters'].items():
                if key not in cls.accepted_filters:
                    invalid_req.add_error(
                            'filters',
                            ("filter '%s' is not valid" % (key))
                    )

            if invalid_req.has_errors():
                return invalid_req

        return cls(filters=adict.get('filters', None))
