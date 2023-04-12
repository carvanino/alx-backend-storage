#!/usr/bin/env python3
"""
Implement an expiring web cache and tracker
"""

import requests
import redis
from functools import wraps

r = redis.Redis()


def count_access(method):
    """
    Decorator to get count for each access to the page
    """
    @wraps(method)
    def wrapper(url):
        html_content = method(url)
        key = "count:{}".format(url)
        r.incr(key)
        cached_key = "cached:{}".format(url)
        cached_response = r.get(cached_key)  # if the url is cached
        if cached_response:
            # print("Already existed")
            return cached_response.decode('utf-8')
        r.setex(cached_key, 10, html_content)
        return html_content
    return wrapper


@count_access
def get_page(url: str) -> str:
    """
    Returns the response from a request on the url
    """
    req = requests.get(url)
    return req.text


'''
url = "http://google.com"
url1 = "https://clip-sync-xo78.vercel.app/login"
print(get_page(url1))
'''
