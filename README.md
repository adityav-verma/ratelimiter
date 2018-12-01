# Rate-Limiter

A python package to have rate limiting for almost anything.

```python
from ratelimiter import RateLimiter

rate_limiter = RateLimiter.redis('host', 'port')

api_request_limit = rate_limiter.limiter(number_of_requests=10, mins=30)

# While performing an action
api_request_limit.is_allowed()  # True/False
api_request_limit.remaining_requests    # Number of requests allowed

```