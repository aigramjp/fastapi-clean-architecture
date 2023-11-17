from typing import Dict, Any, Optional

from .src.database import database
from .src import MongoTools

class UserRepository:

    def find_one_by_user_id(user_id:str) -> Optional[Dict[str, Any]]:
        col = database.get_users_collection()
        return MongoTools.find_one_by_primary_id(col, user_id)

    def insert_one(user: Dict[str, Any]):
        col = database.get_users_collection()
        return MongoTools.insert_one(col, user)

    def delete_one_by_user_id(user_id:str):
        col = database.get_users_collection()
        return MongoTools.delete_one(col, user_id)
