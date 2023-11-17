from pydantic import BaseModel

class RequestPageModel(BaseModel):
    limit: int
    skip: int
