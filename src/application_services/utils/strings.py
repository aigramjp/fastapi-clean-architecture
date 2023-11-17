from uuid import uuid4

class Strings:
    
    @staticmethod
    def random_id():
        return str(uuid4())
