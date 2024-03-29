from .models.request_models import RequestPageModel
from .models.todo_models import TodoDetailedModel
from .models.common_table_model import CommonIdModel

class RequestModels:
    # todo
    class GetTodoModel(CommonIdModel):...
    class DeleteTodoModel(CommonIdModel):...
    class UpdateTodoModel(CommonIdModel, TodoDetailedModel):...
    class GetTodosModel(RequestPageModel):...
    class CreateTodoModel(TodoDetailedModel):...
