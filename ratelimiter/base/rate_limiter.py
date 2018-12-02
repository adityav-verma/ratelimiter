from functools import wraps
from uuid import uuid4

from ..exceptions import RateLimited


class RateLimiter(object):
    """Base class for Rate Limiting"""
    def __init__(self, limit, window, connection):
        """
        :param limit: number of requests allowed
        :type limit: int
        :param window: window in secs in which :limit number requests allowed
        :type window: int
        """
        self._connection = connection
        self._key = str(uuid4())
        self._limit = limit
        self._window = window

    def is_allowed(self, log_current_request=True):
        """
        :param log_current_request: Consider the call for rate limiting
        :type log_current_request: bool
        :return: Whether a requests is allowed or rate limited.
        :rtype: bool
        """
        raise NotImplementedError

    @property
    def remaining_requests(self):
        raise NotImplementedError

    def limit(self, func):
        """Decorator to check the rate limit."""
        @wraps(func)
        def decorated(*args, **kwargs):
            if self.is_allowed():
                return func(*args, **kwargs)
            raise RateLimited
        return decorated
