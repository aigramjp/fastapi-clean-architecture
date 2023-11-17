from pymongo import MongoClient
from pymongo.collection import Collection
from domain_services import IDbController, DbTableEnum

class DbController(IDbController):
    
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

    def get_table(self, table_type:DbTableEnum) -> Collection:
        return self.db[table_type.value]

db_controller = DbController()
