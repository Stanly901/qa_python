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
        assert collector.books_genre[book_name] == ''
        collector.set_book_genre(book_name, 'Фантастика')
        assert collector.books_genre[book_name] == 'Фантастика', (
            f"Жанр книги '{book_name}' должен быть 'Фантастика', "
            f"но в словаре записано '{collector.books_genre[book_name]}'"
        )

    # Тест 3: Получение жанра существующей книги с жанром
    def test_get_book_genre_returns_correct_genre_for_existing_book(self):
        collector = BooksCollector()
        book_name = "Властелин колец"
        collector.books_genre[book_name] = "Фантастика"
        result = collector.get_book_genre(book_name)
        assert result == "Фантастика", (
            f"Метод get_book_genre должен вернуть 'Фантастика' для книги '{book_name}', "
            f"но вернул '{result}'"
        )

    # Тест 4: Получение списка книг по жанру
    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        test_books = [
            ("Война и мир", "Роман"),
            ("1984", "Фантастика"),
            ("Оно", "Ужасы"),
            ("Метро 2033", "Фантастика"),
            ("Шерлок Холмс", "Детективы")
        ]
        for book, genre in test_books:
            collector.add_new_book(book)
            if genre in collector.genre:
                collector.set_book_genre(book, genre)

        genre_to_find = "Фантастика"
        result = collector.get_books_with_specific_genre(genre_to_find)
        expected_books = ["1984", "Метро 2033"]
        assert sorted(result) == sorted(expected_books), (
            f"Ожидались книги {expected_books} с жанром '{genre_to_find}', "
            f"но получено {result}"
        )

    # Тест 5.1: Получение корректного словаря
    def test_get_books_genre_returns_correct_dictionary(self):
        collector = BooksCollector()
        books_to_add = [
            ("Война и мир", "Роман"),
            ("1984", "Фантастика"),
            ("Неизвестная книга", ""),
            ("Оно", "Ужасы")
        ]
        for book, genre in books_to_add:
            collector.add_new_book(book)
            if genre in collector.genre:
                collector.set_book_genre(book, genre)

        result = collector.get_books_genre()
        expected_dict = {
            "Война и мир": "",
            "1984": "Фантастика",
            "Неизвестная книга": "",
            "Оно": "Ужасы"
        }

        assert result == expected_dict, (
            f"Ожидался словарь {expected_dict}, но получено {result}"
        )

    # Тест 5.2: Получение пустого словаря
    def test_get_books_genre_empty(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}

    # Тест 6.1: Получение книг для детей
    def test_get_books_for_children_returns_only_child_friendly_books(self):
        collector = BooksCollector()
        test_books = [
            ("Карлсон", "Мультфильмы"),
            ("Гарри Поттер", "Фантастика"),
            ("Оно", "Ужасы"),
            ("Книга без жанра", ""),
            ("Комедийная книга", "Комедии")
        ]
        for book, genre in test_books:
            collector.add_new_book(book)
            if genre:
                collector.set_book_genre(book, genre)

        result = collector.get_books_for_children()
        expected_child_books = ["Карлсон", "Гарри Поттер", "Комедийная книга"]

        assert sorted(result) == sorted(expected_child_books), (
            f"Ожидались детские книги {expected_child_books}, но получено {result}"
        )

    # Тест 6.2: Книги без жанра не попадают в детские
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