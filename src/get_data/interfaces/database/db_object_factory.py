from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class DbObjectFactory(ABC, Generic[T]):
    @abstractmethod
    def create(self, data: list[dict]) -> list[T]:
        pass