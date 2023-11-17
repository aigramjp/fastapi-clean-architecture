from enum import Enum

class DbTableEnum(str, Enum):
    users = 'users'
    todos = 'todos'
    