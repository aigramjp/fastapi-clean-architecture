from pymongo import MongoClient
from pymongo.collection import Collection

class Database:
    
    def connect(self, **kwargs):
        self.client = MongoClient(
          host=kwargs.get('host'),
          port=kwargs.get('port'),
          username=kwargs.get('username'),
          password=kwargs.get('password'),
        )
        self.db = self.client[kwargs.get('db_name')]

    def disconnect(self):
        if getattr(self, 'client') and isinstance(self.client, MongoClient):
            self.client.close()

    def get_users_collection(self) -> Collection:
        return self.db['users']
  
    def get_todos_collection(self) -> Collection:
        return self.db['todos']

database = Database()
