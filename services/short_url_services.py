from pymongo import MongoClient
from config import Config
from models.short_url import ShortURLModel

class ShortURLService:
    def __init__(self):
        client = MongoClient(Config.MONGO_URI)
        db = client.get_default_database()
        self.model = ShortURLModel(db)

    def delete_short_url(self, short_code):
        result = self.model.delete_short_url(short_code)
        return result.deleted_count > 0

    def get_statistics(self, short_code):
        url_data = self.model.get_statistics(short_code)
        if url_data:
            return {
                "id": str(url_data["_id"]),
                "url": url_data["url"],
                "shortCode": url_data["shortCode"],
                "createdAt": url_data["createdAt"].isoformat(),
                "updatedAt": url_data["updatedAt"].isoformat(),
                "accessCount": url_data["accessCount"]
            }
        return None