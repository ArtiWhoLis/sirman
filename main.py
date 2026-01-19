from src.models.book import Book
from config import Config
from database import load_books_db, add_book_to_db 

new_book = Book ("Гроза", "А. Н. Овстровский", 1859, "978-5-360-09871-3")
add_book_to_db(Config.DB_PATH, new_book)

all_books=load_books_db(Config.DB_PATH)

for book in all_books:
    print(book)
