from enum import Enum

class DbErrorEnum(str, Enum):
    DUPLICATE_KEY_ERROR = 'duplicate key error'
    UNKNOWN_ERROR_BY_INSERT_ONE = 'unknown error by insert one'
    UNKNOWN_ERROR_BY_DELETE_ONE = 'unknown error by delete one'
    NOT_DELETED = 'not deleted'
