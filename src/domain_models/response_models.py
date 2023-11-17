from .models.request_models import RequestPageModel
from .models.todo_models import TodoDetailedModel, TodoOverviewModel
from .models.common_table_model import CommonTableModel
from typing import List
from pydantic import BaseModel

class TodosOverviewTodoModel(TodoOverviewModel, CommonTableModel):...
class TodosOverviewModel(BaseModel):
    todos: List[TodosOverviewTodoModel] = []

class ResponseModels:
    # todo
    class GetTodoModel(TodoDetailedModel, CommonTableModel):...
    class DeleteTodoModel(CommonTableModel):...
    class UpdateTodoModel(TodoDetailedModel, CommonTableModel):...
    class GetTodosModel(TodosOverviewModel):...
    class CreateTodoModel(TodoDetailedModel, CommonTableModel):...