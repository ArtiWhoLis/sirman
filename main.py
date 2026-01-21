from src.models.book import Book
from config import Config
from database import init_db, add_book_to_db, load_books_db

"""
Основной модуль запуска программы.
Создаёт базу (если её нет), добавляет тестовую книгу и выводит список книг.
"""

# 1. Создаём таблицу, если её нет
init_db(Config.DB_PATH)

# 2. Добавляем книгу (можно закомментировать после первого добавления)
new_book = Book("Гроза", "А. Н. Островский", 1859, "978-5-360-09871-3")
add_book_to_db(Config.DB_PATH, new_book)

# 3. Загружаем все книги и выводим
all_books = load_books_db(Config.DB_PATH)
for book in all_books:
	print(book)