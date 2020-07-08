import logging


class WeblibError(Exception):
    """
    Base class for all custom exceptions
    defined in weblib package.
    """

class ResponseNotValid(WeblibError):
    """
    Indicates unexpected data received in the
    result of network request.
    """


class DataNotValid(ResponseNotValid):
    pass


class DataNotFound(WeblibError, IndexError):
    pass


class RequiredDataNotFound(DataNotFound):
    pass
