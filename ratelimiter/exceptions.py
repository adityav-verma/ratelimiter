class CustomException(Exception):
    def __init__(self, message):
        super(CustomException, self).__init__(message)


class DatastoreConnectionError(CustomException):
    def __init__(self):
        message = 'Could not establish connection to data store'
        super(DatastoreConnectionError, self).__init__(message)
