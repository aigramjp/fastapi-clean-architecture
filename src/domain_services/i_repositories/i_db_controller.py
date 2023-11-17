import abc
from typing import Dict, Any
from ..enums.db_table_enum import DbTableEnum

class IDbController(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def connect(**kwargs:Dict[str, Any]):
        raise NotImplementedError()

    @abc.abstractmethod
    def disconnect():
        raise NotImplementedError()

    @abc.abstractmethod
    def get_table(table_type:DbTableEnum):
        raise NotImplementedError()
