from fastapi import APIRouter

from .todo_routes import routes as todo_routes

routes = APIRouter()
routes.include_router(todo_routes)
