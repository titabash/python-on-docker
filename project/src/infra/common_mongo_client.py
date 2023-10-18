from pymongo import MongoClient
import os


class CommonMongoClient:
    def __init__(self, dbName, collectionName, user=None, pwd=None, port=27017):
        self.client = MongoClient(os.environ["MONGO_ENDPOINT"], port)
        user = user if user is not None else os.environ["MONGO_USER"]
        pwd = pwd if pwd is not None else os.environ["MONGO_PASS"]
        self.client[dbName].authenticate(user, pwd)
        self.db = self.client[dbName]  # DB名を設定
        self.collection = self.db.get_collection(collectionName)
