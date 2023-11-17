from .delete_one import DeleteOne
from .find import Find
from .find_one import FindOne
from .insert_one import InsertOne
from .update_one import UpdateOne

class MongoTools(DeleteOne, Find, FindOne, InsertOne, UpdateOne):
  ...
