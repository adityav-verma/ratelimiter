import redis
from uuid import uuid4


class RateLimiterMixin(object):
    """Interface for a rate limiter"""
    def is_allowed(self):
        raise NotImplementedError

    @property
    def remaining_requests(self):
        return self._allowed_requests - self._remaining_requests

    @property
    def allowed_requests(self):
        return self._allowed_requests


class CustomException(Exception):
    def __init__(self, message):
        super(CustomException, self).__init__(message)


class DatastoreConnectionError(CustomException):
    def __init__(self):
        message = 'Could not establish connection to data store'
        super(DatastoreConnectionError, self).__init__(message)


class RedisRateLimiter(RateLimiterMixin):
    def __init__(self, allowed, window, connection):
        self.connection = connection
        self.key = uuid4()
        self._allowed_requests = allowed
        self._window = window
        self._remaining_requests = 0

    def is_allowed(self):
        raise NotImplementedError


class RedisRateLimiterConnection(object):
    def __init__(self, host=None, port=None, connection=None):
        self.connection = None
        if host and port:
            connection = redis.StrictRedis(host, port)
            if not connection.ping():
                raise DatastoreConnectionError
            self.connection = connection
        elif connection:
            if not connection.ping():
                raise DatastoreConnectionError
            self.connection = connection
        else:
            raise DatastoreConnectionError

    def get_instance(self, allowed, seconds=None, minutes=None, hours=None):
        if seconds:
            window = seconds
        elif minutes:
            window = minutes * 60
        elif hours:
            window = hours * 60 * 60
        else:
            raise Exception
        return RedisRateLimiter(allowed, window, self.connection)


class Limiter(object):
    def __init__(self):
        pass

    @classmethod
    def redis(cls, host='localhost', port=6379, connection=None):
        """Create an instance of a redis based rate limiter"""
        return RedisRateLimiterConnection(
            host=host, port=port, connection=connection
        )
