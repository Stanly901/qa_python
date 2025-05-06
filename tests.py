from main import BooksCollector

class TestBooksCollector:

    # Тест 1: Добавление одной книги
    def test_add_new_book_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        assert len(collector.get_books_genre()) == 1

    # Тест 2: Установка жанра для существующей книги
    def test_set_book_genre_for_existing_book(self):
        collector = BooksCollector()
        book_name = 'Дюна'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Фантастика')
        assert collector.get_book_genre(book_name) == 'Фантастика'

    # Тест 3: Получение жанра существующей книги без жанра (пустая строка)
    def test_get_book_genre_for_book_without_genre(self):
        collector = BooksCollector()
        book_name = 'Анна Каренина'
        collector.add_new_book(book_name)
        assert collector.get_book_genre(book_name) == ''

    # Тест 4: Получение списка книг по жанру
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        books = ['Книга 1', 'Книга 2']
        genre = 'Ужасы'
        for book in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        assert collector.get_books_with_specific_genre(genre) == books

    # Тест 5: Получение пустого словаря, когда нет книг
    def test_get_books_genre_empty(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}

    # Тест 6: Книги без жанра не должны попадать в детские
    def test_books_without_genre_not_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Книга без жанра")
        assert collector.get_books_for_children() == []

    # Тест 7: Добавление книги в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        book_name = 'Мастер и Маргарита'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    # Тест 8: Удаление книги из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        book_name = 'Преступление и наказание'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    # Тест 9: Получение списка избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        favorites = ['Книга 1', 'Книга 2']
        for book in favorites:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)
        assert set(collector.get_list_of_favorites_books()) == set(favorites)