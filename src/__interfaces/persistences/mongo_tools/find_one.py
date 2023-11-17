from typing import Dict, Any

from pymongo.collection import Collection

class FindOne:
    def find_one_by_filter(col:Collection, filter:Dict[str, Any]):
        
        try:
            return col.find_one(filter)
        except:
            pass

    def find_one_by_primary_id(col:Collection, _id:str):
      return FindOne.find_one_by_filter(col, {'_id': _id})
