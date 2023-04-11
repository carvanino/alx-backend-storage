#!/usr/bin/env python3
"""
Working with mongo and python 1 - Inserting
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new documents in mongo_collection from kwargs
    """
    newDocuments = mongo_collection.insert_many([kwargs])
    return newDocuments.inserted_ids
