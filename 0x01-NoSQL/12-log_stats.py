#!/usr/bin/env python3
"""
Stats from Nginx logs stored in MongoDB
"""
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client["logs"]


log = db.nginx.count_documents({})
get = db.nginx.count_documents({"method": "GET"})
post = db.nginx.count_documents({"method": "POST"})
put = db.nginx.count_documents({"method": "PUT"})
patch = db.nginx.count_documents({"method": "PATCH"})
delete = db.nginx.count_documents({"method": "DELETE"})
status_check = db.nginx.count_documents(
    {"$and": [{"method": "GET"}, {"path": "/status"}]})

'''
log = db.nginx.find({}).count()
get = db.nginx.find({method: "GET"}).count()
post = db.nginx.find({method: "POST"}).count()
put = db.nginx.find({method: "PUT"}).count()
patch = db.nginx.find({method: "PATCH"}).count()
delete = db.nginx.find({method: "DELETE"}).count()

status_check = db.nginx.find(
        {"$and": [{"method": "GET"}, {"path": "/status"}]}).count()
'''
print('{} logs\n\
Methods:\n\
\tmethod GET: {}\n\
\tmethod POST: {}\n\
\tmethod PUT: {}\n\
\tmethod PATCH: {}\n\
\tmethod DELETE: {}\n\
{} status check\
'.format(log, get, post, put, patch, delete, status_check)
      )
