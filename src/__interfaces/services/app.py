from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from adapters.gateways import connect, disconnect
from .utils.env import env
from .routers import routers

def get_app():
    app = FastAPI(title='PROJECT_NAME')
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(routers)
    app.add_event_handler("startup", lambda: connect(
        host=env.DB_HOST, 
        port=env.DB_PORT, 
        username=env.DB_USERNAME, 
        password=env.DB_PASSWORD, 
        db_name=env.DB_NAME
    ))
    app.add_event_handler("shutdown", disconnect)
