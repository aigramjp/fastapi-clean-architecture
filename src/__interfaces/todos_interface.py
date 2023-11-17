from .src.database import database
from .src import MongoTools

class TodosRepository:

    def find_todo_list(
            skip:int, 
            limit:int, 
            sort_key:str='created_at', 
            sort_direction:int=-1
        ):
        col = database.get_todos_collection()
        return MongoTools.find(
            col, 
            skip, 
            limit, 
            sort_key=sort_key, 
            sort_direction=sort_direction
        )
