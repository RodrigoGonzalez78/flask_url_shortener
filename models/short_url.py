from pymongo import MongoClient
from datetime import datetime

class ShortURLModel:
    def __init__(self, db):
        self.collection = db['short_urls']

    def create_short_url(self, url, short_code):
        short_url = {
            "url": url,
            "shortCode": short_code,
            "createdAt": datetime.utcnow(),
            "updatedAt": datetime.utcnow(),
            "accessCount": 0
        }
        return self.collection.insert_one(short_url).inserted_id

    def find_by_short_code(self, short_code):
        return self.collection.find_one({"shortCode": short_code})

    def update_access_count(self, short_code):
        return self.collection.update_one(
            {"shortCode": short_code},
            {"$inc": {"accessCount": 1}, "$set": {"updatedAt": datetime.utcnow()}}
        )

    def delete_short_url(self, short_code):
        return self.collection.delete_one({"shortCode": short_code})

    def get_statistics(self, short_code):
        return self.collection.find_one({"shortCode": short_code})