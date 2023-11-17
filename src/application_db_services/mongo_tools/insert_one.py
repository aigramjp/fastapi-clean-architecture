from pymongo.collection import Collection
from pymongo.errors import DuplicateKeyError

from domain_services import DbErrorEnum
from .utils import convert_from_id_to_primary_key
from pydantic import BaseModel
from typing import Optional

class InsertOne:
    def insert_one(col:Collection, data:BaseModel) -> Optional[DbErrorEnum]:

        try:
            col.insert_one(convert_from_id_to_primary_key(data.dict()))
        except DuplicateKeyError:
            return DbErrorEnum.DUPLICATE_KEY_ERROR
        except Exception:
            return DbErrorEnum.UNKNOWN_ERROR_BY_INSERT_ONE
