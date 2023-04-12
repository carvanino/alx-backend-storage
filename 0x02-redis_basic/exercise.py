#!/usr/bin/env python3
"""
Reading from Redis by type
"""

import redis
from uuid import uuid4
from functools import wraps
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """
    increments a counter for each time a method on Cache is called

    """
    @wraps(method)
    def count_wrapper(self, data):
        # func = method(*args, **kwargs)
        key = method.__qualname__
        self._redis.incr(key)
        return self._redis.get(key)
        # return func
    return count_wrapper


class Cache:
    """
    A Cache class
    """

    def __init__(self, host='localhost', port=6379,
                 db=0, password=None) -> None:
        """
        Instantiates the class
        """

        self._redis = redis.Redis(host=host, port=port, password=password)
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key using uuid
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]
            = None) -> Union[str, bytes, int]:
        """
        Converts a data to the desired format(str, int or byte)
        """
        if not self._redis.get(key):
            return None
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """
        Parametrize to str
        """
        # value = self._redis.get(str(key))
        value = self.get(key, lambda d: d.decode('utf-8'))
        return value

    def get_int(self, key: str) -> int:
        """
        Parametrize to int
        """
        # key = self._redis.get(int(key))
        value = self.get(key, int)
        return value
