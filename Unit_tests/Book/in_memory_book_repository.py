from book_repository import BookRepository
from book import Book
from collections import defaultdict
from typing import List


class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self.books = defaultdict(Book)
        self.books["1"] = Book("1", "Book1", "Author1")
        self.books["2"] = Book("2", "Book2", "Author2")

    def find_by_id(self, id_book: str) -> 'Book':
        return self.books.get(id_book)

    def find_all(self) -> List['Book']:
        return list(self.books.values())
