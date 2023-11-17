from .delete_one import DeleteOne
from .find import Find
from .find_one import FindOne
from .insert_one import InsertOne

class MongoTools(DeleteOne, Find, FindOne, InsertOne):
  ...
