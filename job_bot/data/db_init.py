from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import bson
import os

load_dotenv()
uri = os.getenv('DATABASE_URL',)
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['user']
coll = db['users']
coll.drop()

with open('job_bot/data/sample_collection.bson', 'rb') as bson_file:
    bson_data = bson.decode_all(bson_file.read())
    coll.insert_many(bson_data)
