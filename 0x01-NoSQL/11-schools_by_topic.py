#!/usr/bin/env python3
"""
working with Mongo and Python 3 - Finding with conditions
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topics
    Args:
        <mongo_collection>: pymongo collection object
        <topic>: string
    Returns:
        List
    """

    schools = mongo_collection.find({"topics": topic})
    return schools
