from typing import Dict, Any

from pymongo.collection import Collection
from pymongo.errors import DuplicateKeyError

from ..error_enums import ErrorEnums
from .utils import convert_from_id_to_primary_key

class InsertOne:
    def insert_one(col:Collection, data:Dict[str, Any]):

        try:
            col.insert_one(convert_from_id_to_primary_key(data))
        except DuplicateKeyError:
            return ErrorEnums.DUPLICATE_KEY_ERROR
        except Exception:
            return ErrorEnums.UNKNOWN_ERROR_BY_INSERT_ONE
