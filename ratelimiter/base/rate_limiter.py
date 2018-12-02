from uuid import uuid4


class RateLimiter(object):
    """Base class for Rate Limiting"""
    def __init__(self, limit, window, connection):
        """
        :param limit: number of requests allowed
        :type limit: int
        :param window: window in secs in which :limit number requests allowed
        :type window: int
        """
        self.connection = connection
        self.key = uuid4()
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

    @property
    def limit(self):
        """Total number of requests allowed"""
        return self._limit
