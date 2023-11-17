from fastapi import APIRouter
from ..constants import Endpoints

from domain_models import TableModels
from application_db_services import db_controller, TodoTableController
from application_services import TodoUseCase, TodosUseCase
from domain_models import RequestModels, ResponseModels

tags = ['TODO']

class Response(TableModels.TodoTableModel):
    message: str = ''

routes = APIRouter()

# create todo

@routes.post(
    Endpoints.Todo.create_todo,
    tags=tags,
    response_model=ResponseModels.CreateTodoModel
)
async def endpoint(
    req: RequestModels.CreateTodoModel,
):
  todo_table_controller = TodoTableController(db_controller)
  return TodoUseCase.create_todo(todo_table_controller, req)

# delete todo

@routes.post(
    Endpoints.Todo.delete_todo,
    tags=tags,
    response_model=ResponseModels.DeleteTodoModel
)
async def endpoint(
    req: RequestModels.DeleteTodoModel,
):
  todo_table_controller = TodoTableController(db_controller)
  return TodoUseCase.delete_todo(todo_table_controller, req)

# get todos

@routes.post(
    Endpoints.Todo.get_todos,
    tags=tags,
    response_model=ResponseModels.GetTodosModel
)
async def endpoint(
    req: RequestModels.GetTodosModel,
):
  todo_table_controller = TodoTableController(db_controller)
  return TodosUseCase.get_todos(todo_table_controller, req)

# update todo

@routes.post(
    Endpoints.Todo.update_todo,
    tags=tags,
    response_model=ResponseModels.UpdateTodoModel
)
async def endpoint(
    req: RequestModels.UpdateTodoModel,
):
  todo_table_controller = TodoTableController(db_controller)
  return TodoUseCase.update_todo(todo_table_controller, req)

# get todo

@routes.post(
    Endpoints.Todo.get_todo,
    tags=tags,
    response_model=ResponseModels.GetTodoModel
)
async def endpoint(
    req: RequestModels.GetTodoModel,
):
  todo_table_controller = TodoTableController(db_controller)
  return TodoUseCase.get_todo(todo_table_controller, req)


