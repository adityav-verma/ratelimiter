# Rate-Limiter

A python package for sliding window rate limiting.

The current backend supported is Redis. However, more backends are to be added in future.
### Usage
```python
from ratelimiter import Limiter

limiter = RateLimiter.redis('host', 'port')

# `rate_limiter_1` will check for 10 requests in a sliding window of 5 mins
rate_limiter_1 = limiter.get_instance(limit=10, secs=300)

# `rate_limiter_2` will check for 5 requests in a sliding window of 2 mins
rate_limiter_2 = limiter.get_instance(limit=5, minutes=2)

# While performing an action
rate_limiter_1.is_allowed()  # True/False
```
