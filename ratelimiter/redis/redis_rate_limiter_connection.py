import redis

from ..exceptions import DatastoreConnectionError
from .redis_rate_limiter import RedisRateLimiter


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
