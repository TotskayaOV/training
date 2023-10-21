from .book_repository import BookRepository
from typing import List


class BookService:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def find_book_by_id(self, id_book: str) -> 'Book':
        return self.book_repository.find_by_id(id_book)

    def find_all_books(self) -> List['Book']:
        return self.book_repository.find_all()
