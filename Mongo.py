from pymongo import MongoClient
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()
cluster = MongoClient(os.getenv('mongo_cluster_key'))
db = cluster["Identiyy"]
collection = db["Users"]


def updateMogoUserCollection(name, age, country):
    user_temp = {"name":name, "age":age , "country": country}
    collection.insert_one(user_temp)
