from abc import ABC, abstractmethod
from typing import List


class BookRepository(ABC):

    @abstractmethod
    def find_by_id(self, id_book: str) -> 'Book':
        pass

    @abstractmethod
    def find_all(self) -> List['Book']:
        pass
