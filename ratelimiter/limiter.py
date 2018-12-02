from .redis import RedisRateLimiterConnection


class Limiter(object):
    def __init__(self):
        pass

    @classmethod
    def redis(cls, host='localhost', port=6379, connection=None):
        """Create an instance of a redis based rate limiter"""
        return RedisRateLimiterConnection(
            host=host, port=port, connection=connection
        )