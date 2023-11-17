from typing import Dict, Any

from pymongo.collection import Collection
from .utils import convert_from_primary_key_to_id

class FindOne:
    def find_one_by_filter(col:Collection, filter:Dict[str, Any]) -> Dict[str, Any]:
        
        try:
            item = col.find_one(filter)
            return item if item else {}
        except:
            return {}

    def find_one_by_primary_id(col:Collection, _id:str) -> Dict[str, Any]:
      item = FindOne.find_one_by_filter(col, {'_id': _id})
      return convert_from_primary_key_to_id(item)
