from typing import Dict, Any

def convert_from_id_to_primary_key(data:Dict[str, Any]):
    return {
        k if k!='id' else '_id':v 
        for k,v in data.items()
    }

def convert_from_primary_key_to_id(data:Dict[str, Any]):
    return {
        k if k!='_id' else 'id':v 
        for k,v in data.items()
    }
