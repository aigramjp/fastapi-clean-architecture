from pymongo.collection import Collection

class Find:
    
    def find(
        col:Collection, 
        skip:int, 
        limit:int, 
        sort_key:str, 
        sort_direction:int
    ):
        
        try:
            return list(
                col
                  .find({})
                  .sort(sort_key, sort_direction)
                  .skip(skip)
                  .limit(limit)
            )
        except Exception as e:
            print(e)
            return []