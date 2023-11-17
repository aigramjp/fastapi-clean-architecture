import os
from pydantic import BaseModel

class Env(BaseModel):
    DB_NAME: str
    DB_HOST: str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_PORT: int

env = Env(**os.environ)
