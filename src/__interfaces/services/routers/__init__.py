from fastapi import APIRouter
from pydantic import BaseModel

routers = APIRouter()

class Request(BaseModel):
    ...

class Response(BaseModel):
    message: str = ''

router = APIRouter()
@router.post(
    '/test',
    response_model=Response
)
async def endpoint(
    req: Request,
):
  return {}

routers.include_router(router)
