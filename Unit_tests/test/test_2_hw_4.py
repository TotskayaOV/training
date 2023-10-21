import pytest
from pytest_mock import MockFixture
from Unit_tests.Book import BookService, Book, BookRepository

def test_find_book_by_id(mocker: MockFixture):
    # создаем мок-объект BookRepository
    book_repository_mock = mocker.Mock(spec=BookRepository)
    book_repository_mock.find_by_id.return_value = Book("1", "Book1", "Author1")

    # создаем экземпляр BookService с мок-объектом BookRepository
    book_service = BookService(book_repository_mock)

    # вызываем find_book_by_id()
    result = book_service.find_book_by_id("1")

    # проверяем, что метод find_by_id() был вызван с правильными аргументами
    book_repository_mock.find_by_id.assert_called_once_with("1")

    # проверяем, что find_book_by_id() вернул ожидаемый результат
    assert result == Book("1", "Book1", "Author1")

def test_find_all_books(mocker: MockFixture):
    # создаем мок-объект BookRepository
    book_repository_mock = mocker.Mock(spec=BookRepository)
    book_repository_mock.find_all.return_value = [
        Book("1", "Book1", "Author1"),
        Book("2", "Book2", "Author2")
    ]

    # создаем экземпляр BookService с мок-объектом BookRepository
    book_service = BookService(book_repository_mock)

    # вызываем find_all_books()
    result = book_service.find_all_books()

    # проверяем, что find_all() был вызван
    book_repository_mock.find_all.assert_called_once()

    # проверяем, что find_all_books вернул ожидаемый результат
    assert result == [
        Book("1", "Book1", "Author1"),
        Book("2", "Book2", "Author2")
    ]
