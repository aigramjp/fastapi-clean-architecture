
from pymongo.collection import Collection

from ..error_enums import ErrorEnums


class DeleteOne:
    
    def delete_one(col:Collection, _id:str):
        
        try:
            res = col.delete_one({'_id': _id})
            if not res.deleted_count:
                return ErrorEnums.NOT_DELETED

        except Exception:
            return ErrorEnums.UNKNOWN_ERROR_BY_DELETE_ONE
    
