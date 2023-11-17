from pymongo.collection import Collection
from domain_services import DbErrorEnum

class DeleteOne:
    
    def delete_one(col:Collection, _id:str):
        
        try:
            res = col.delete_one({'_id': _id})
            if not res.deleted_count:
                return DbErrorEnum.NOT_DELETED

        except Exception:
            return DbErrorEnum.UNKNOWN_ERROR_BY_DELETE_ONE
    
