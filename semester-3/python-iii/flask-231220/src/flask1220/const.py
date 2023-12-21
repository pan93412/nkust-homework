import os
import pymongo


client = pymongo.MongoClient(os.environ["MONGO_URI"])
db = client["flask1220"]
collection = db["users"]
