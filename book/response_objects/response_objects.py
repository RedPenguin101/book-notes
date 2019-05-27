# response_objects.py


class ResponseSuccess:
    SUCCESS = 'Success'

    def __init__(self, value=None):
        self.type = self.SUCCESS
        self.value = value

    def __bool__(self):
        return True


class ResponseFailure:
    PARAMETERS_ERROR = 'ParametersError'
    RESOURCE_ERROR = 'ResourceError'
    SYSTEM_ERROR = 'SystemError'

    def __init__(self, type, message):
        self.type = type
        self.message = self._format_message(message)

    def _format_message(self, message):
        if isinstance(message, Exception):
            return ": ".join((message.__class__.__name__, format(message)))
        return message

    @property
    def value(self):
        return {'type': self.type, 'message': self.message}

    @classmethod
    def build_response_from_invalid_request(cls, request):
        type = cls.PARAMETERS_ERROR
        message = "\n".join([": ".join(
                      [err['parameter'], err['message']]
                  ) for err in request.errors])

        return cls(type, message)

    @classmethod
    def build_parameter_failure(cls, message):
        return cls(cls.PARAMETERS_ERROR, message)

    @classmethod
    def build_resource_failure(cls, message):
        return cls(cls.RESOURCE_ERROR, message)

    @classmethod
    def build_system_failure(cls, message):
        return cls(cls.SYSTEM_ERROR, message)

    def __bool__(self):
        return False
