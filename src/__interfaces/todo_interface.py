from typing import Dict, Any, Optional

from .database import database
from .mongo_tools import MongoTools

class TodoRepository:

    def find_one_by_todo_id(todo_id:str) -> Optional[Dict[str, Any]]:
        col = database.get_todos_collection()
        return MongoTools.find_one_by_primary_id(col, todo_id)

    def insert_one(todo: Dict[str, Any]):
        col = database.get_todos_collection()
        return MongoTools.insert_one(col, todo)

    def delete_one_by_todo_id(todo_id:str):
        col = database.get_todos_collection()
        return MongoTools.delete_one(col, todo_id)
