from ..base.rate_limiter import RateLimiter


class RedisRateLimiter(RateLimiter):
    def __init__(self, allowed, window, connection):
        super(RedisRateLimiter, self).__init__(allowed, window, connection)

    def is_allowed(self):
        raise NotImplementedError
