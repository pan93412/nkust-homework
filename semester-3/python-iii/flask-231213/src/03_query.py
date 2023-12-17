import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["owo"]
mycol = mydb["users"]

key = input("Enter a key: ")
value = input("Enter a value: ")

for x in mycol.find({key: value}):
    print(x)
