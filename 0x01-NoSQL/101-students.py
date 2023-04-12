#!/usr/bin/env python3
"""
Aggregate operations
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    Args:
        <mongo_collection>: pymongo collection object
    """
    # mongo_collection.find({topics: $avg(score)})
    avg = mongo_collection.aggregate(
        [
            {"$project":
             {"name": "$name", "averageScore":
              {"$avg": "$topics.score"}
              }
             },
            {"$sort":
             {"averageScore": -1}
             }
        ]
    )
    return list(avg)
