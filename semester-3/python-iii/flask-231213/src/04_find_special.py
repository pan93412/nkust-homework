import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["owo"]
mycol = mydb["users"]

print("---- age>20 ----")

for x in mycol.find({"age": {"$gt": 20}}):
    print(x)

print("---- name>E ----")

for x in mycol.find({"name": {"$gt": "F"}}):
    print(x)

print("---- E 開頭 ----")

for x in mycol.find({"name": {"$regex": "^E"}}):
    print(x)
