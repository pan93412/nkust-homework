#!/usr/bin/env python3

from typing import Generator
import pymongo
import bson
import random

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["owo"]

names = ["John", "Jane", "Michael", "Emily", "David", "Olivia"]
domains = ["gmail.com", "yahoo.com", "hotmail.com"]
hobbies = ["programming", "gaming", "reading", "sports"]


def gendata() -> Generator[dict, None, None]:
    for _ in range(15):
        name = random.choice(names)
        email = f"{name.lower()}@{random.choice(domains)}"
        age = random.randint(18, 60)
        random.shuffle(hobbies)
        yield {
            "id": bson.ObjectId(),
            "name": name,
            "email": email,
            "age": age,
            "hobbies": hobbies[:3]
        }

# Insert a document into the collection
db["users"].insert_many(gendata())
