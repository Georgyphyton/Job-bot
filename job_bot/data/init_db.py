from active_db import coll
import bson

coll.drop()
with open('job_bot/data/sample_collection.bson', 'rb') as bson_file:
    bson_data = bson.decode_all(bson_file.read())
    coll.insert_many(bson_data)
