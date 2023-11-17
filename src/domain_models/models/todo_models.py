from pydantic import BaseModel
from typing import Optional, List
from ..enums.error_enum import ErrorEnum

class TodoTitleModel(BaseModel):
    title: Optional[str]

    def check_title_format(self) -> Optional[ErrorEnum]:
        if self.title and len(self.title) > 40:
            return ErrorEnum.TOO_LONG_TITLE

class TodoDescriptionModel(BaseModel):
    description: Optional[str]

    def check_description_format(self) -> Optional[ErrorEnum]:
        if self.description and len(self.description) > 200:
            return ErrorEnum.TOO_LONG_DESCRIPTION

class TodoOverviewModel(TodoTitleModel, TodoDescriptionModel):...
class TodoDetailedModel(TodoOverviewModel):...
