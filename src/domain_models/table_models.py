
from .models.common_table_model import CommonTableModel
from .models.todo_models import TodoTitleModel, TodoDescriptionModel
from .models.auth_models import AuthEmailModel, AuthPasswordModel

class TableModels:
  class TodoTableModel(CommonTableModel, TodoTitleModel, TodoDescriptionModel):...
  class UserTableModel(CommonTableModel, AuthEmailModel, AuthPasswordModel):...
