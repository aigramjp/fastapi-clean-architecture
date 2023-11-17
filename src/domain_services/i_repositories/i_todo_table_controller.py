import abc
from typing import Optional
from .i_db_controller import IDbController
from ..enums.db_error_enum import DbErrorEnum
from domain_models import TableModels

class ITodoTableController(metaclass=abc.ABCMeta):
    
    def __init__(self, db:IDbController):
        raise NotImplementedError()
    
    def find_one_by_todo_id(self, todo_id:str) -> TableModels.TodoTableModel:
        raise NotImplementedError()

    def insert_one(self, todo: TableModels.TodoTableModel) -> Optional[DbErrorEnum]:
        raise NotImplementedError()

    def delete_one_by_todo_id(self, todo_id:str) -> Optional[DbErrorEnum]:
        raise NotImplementedError()
    
    def update_one_by_todo_id(self, todo_id: str, todo: TableModels.TodoTableModel) -> TableModels.TodoTableModel:
        raise NotImplementedError()
    
    def find(self, skip: int, limit: int, sort_key: str, sort_direction: int):
        raise NotImplementedError()