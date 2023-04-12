#!/usr/bin/env python3
"""

"""

import redis
from uuid import uuid4
from typing import Union

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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key using uuid
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
