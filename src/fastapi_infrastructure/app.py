from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .constants import env
from .routes import routes
from application_db_services import db_controller

def get_app():
    app = FastAPI(title='PROJECT_NAME')
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(routes)

    app.add_event_handler("startup", lambda: db_controller.connect(
        host=env.DB_HOST, 
        port=env.DB_PORT, 
        username=env.DB_USERNAME, 
        password=env.DB_PASSWORD, 
        db_name=env.DB_NAME
    ))
    app.add_event_handler("shutdown", db_controller.disconnect)
  
    return app

