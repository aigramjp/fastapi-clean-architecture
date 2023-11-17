from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CommonIdModel(BaseModel):
    id: Optional[str] = None

    def check_id_exists(self):
        if not self.id:
            return 'error'

class CommonTableModel(CommonIdModel):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
