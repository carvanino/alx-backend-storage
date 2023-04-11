#!/usr/bin/env python3
"""
Working with mongo and python 2 - Updating Documents
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school documents based on the name
    Args:
        <mongo_collection>: pymongo collection object
        <name>: string
        <topics>: List[string]
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
