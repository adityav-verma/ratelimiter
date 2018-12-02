import time

from ..base.rate_limiter import RateLimiter


class RedisRateLimiter(RateLimiter):
    def __init__(self, allowed, window, connection):
        super(RedisRateLimiter, self).__init__(allowed, window, connection)
        self._pipeline = self._connection.pipeline()

    def _increment_request(self):
        key_value = int(time.time()) + self._window
        self._pipeline.zadd(
            self._key, {key_value: key_value},
        )
        self._pipeline.execute()

    def is_allowed(self, log_current_request=True):
        if log_current_request:
            self._increment_request()
        current_time = time.time()
        self._pipeline.zremrangebyscore(self._key, '-inf', current_time)
        self._pipeline.zcount(self._key, '-inf', '+inf')
        result = self._pipeline.execute()
        return result[-1] <= self._limit
