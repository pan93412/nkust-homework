import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["owo"]
mycol = mydb["users"]

qemail = input("Enter the email to query: ")

print(f"---- email > {qemail} ----")

for x in mycol.find({"email": {"$gt": qemail}}):
    print(x)

print(f"---- email < {qemail} ----")

for x in mycol.find({"email": {"$lt": qemail}}):
    print(x)

print(f"---- email = {qemail} 開頭 ----")

for x in mycol.find({"email": {"$regex": "^"+qemail}}):
    print(x)

print(f"---- age = between 30-50 ----")

for x in mycol.find({"$and": [{"$gte": 30}, {"$lte": 50}]}):
    print(x)
