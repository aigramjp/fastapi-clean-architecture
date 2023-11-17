from typing import Dict, Any

from pymongo.collection import Collection
from .utils import convert_from_primary_key_to_id
from pydantic import BaseModel

class UpdateOne:

    def update_one_by_primary_id(col:Collection, _id:str, data:BaseModel) -> Dict[str, Any]:
      item = col.find_one_and_update(
         {'_id':_id},
         {'$set':convert_from_primary_key_to_id(data.dict(exclude_unset=True))}
      )
      return convert_from_primary_key_to_id(item)
