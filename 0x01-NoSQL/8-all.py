#!/usr/bin/env/ python3
"""
Working with mongo and python 0
"""


import pymongo


def list_all(mongo_collection):
    """
    Lists all documents in a collection
    """
    document = mongo_collection.find({})
    if not document:
        return []
    return list(document)
