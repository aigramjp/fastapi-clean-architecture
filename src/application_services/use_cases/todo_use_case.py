from typing import Optional
from ..utils import Strings, Moment

from domain_models import TableModels
from domain_services import ITodoTableController
from domain_models import ResponseModels, RequestModels

class TodoUseCase:
    
    @staticmethod
    def create_todo(
        todo_table_controller: ITodoTableController,
        req:RequestModels.CreateTodoModel,
    ):

        todo = TableModels.TodoTableModel(
            id=Strings.random_id(),
            created_at=Moment.timestamp(),
            updated_at=Moment.timestamp(),
            title=req.title, 
            description=req.description
        )

        err = todo.check_title_format()
        err = todo.check_description_format()

        err = todo_table_controller.insert_one(todo)

        return ResponseModels.CreateTodoModel(**todo)

    @staticmethod
    def get_todo(
        todo_table_controller: ITodoTableController,
        req: RequestModels.GetTodoModel,
    ):
        todo = todo_table_controller.find_one_by_todo_id(req.id)

        err = todo.check_id_exists()

        return ResponseModels.GetTodoModel(**todo)

    @staticmethod
    def delete_todo(
        todo_table_controller: ITodoTableController,
        req: RequestModels.DeleteTodoModel,        
    ):
        err = todo_table_controller.delete_one_by_todo_id(req.id)

        todo = todo_table_controller.find_one_by_todo_id(req.id)

        return ResponseModels.DeleteTodoModel(**todo)
    
    @staticmethod
    def update_todo(
        todo_table_controller: ITodoTableController,
        req: RequestModels.UpdateTodoModel,        
    ):

        todo = TableModels.TodoTableModel(
            updated_at=Moment.timestamp(),
            title=req.title, 
            description=req.description
        )

        updated_todo = todo_table_controller.update_one_by_todo_id(req.id, todo)
        return ResponseModels.UpdateTodoModel(**updated_todo)