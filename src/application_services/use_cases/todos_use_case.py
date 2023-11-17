from domain_services import ITodoTableController
from domain_models import ResponseModels, RequestModels

class TodosUseCase:
    
    @staticmethod
    def get_todos(
        todo_table_controller: ITodoTableController,
        req: RequestModels.GetTodosModel,
    ):
        todos = todo_table_controller.find(
            skip=req.skip,
            limit=req.limit,
            sort_key='created_at',
            sort_direction=-1,
        )

        return ResponseModels.GetTodosModel(todos=todos)
