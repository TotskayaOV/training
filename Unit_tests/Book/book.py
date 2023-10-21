class Book:

    def __init__(self, id_book: str, title: str, author: str):
        self.id_book = id_book
        self.title = title
        self.author = author

    def __eq__(self, other):
        if isinstance(other, Book):
            return all([self.id_book == other.id_book, self.title == other.title, self.author == other.author])
