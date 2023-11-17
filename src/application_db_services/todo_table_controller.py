from domain_models import TableModels
from domain_services import ITodoTableController, IDbController, DbTableEnum

from .mongo_tools import MongoTools

class TodoTableController(ITodoTableController):
    
    def __init__(self, db:IDbController):
        self.table = db.get_table(DbTableEnum.todos)        

    def find_one_by_todo_id(self, todo_id:str):
        return MongoTools.find_one_by_primary_id(self.table, todo_id)

    def insert_one(self, todo: TableModels.TodoTableModel):
        return MongoTools.insert_one(self.table, todo)

    def delete_one_by_todo_id(self, todo_id:str):
        return MongoTools.delete_one(self.table, todo_id)

    def update_one_by_todo_id(self, todo_id:str, todo:TableModels.TodoTableModel):
        return MongoTools.update_one_by_primary_id(self.table, todo_id, todo)
    
    def find(self, skip: int, limit: int, sort_key: str, sort_direction: int):
        return MongoTools.find(self.table, skip, limit, sort_key, sort_direction)
    