import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["owo"]
mycol = mydb["users"]

for x in mycol.find({}, {"_id": 0}):
    print(x)
