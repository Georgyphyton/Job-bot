from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()
uri = os.getenv('DATABASE_URL',)
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['user']
coll = db['users']

if coll.find_one():
    min_time = list(coll.aggregate(
        [{"$group": {"_id": 1, "min_time": {"$min": "$dt"}}}]))[0]['min_time']
    max_time = list(coll.aggregate(
        [{"$group": {"_id": 1, "max_time": {"$max": "$dt"}}}]))[0]['max_time']
