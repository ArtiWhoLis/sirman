import sqlite3
from src.models import Book

def load_books_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT title, author, year, isbn FROM books")
    books = []
    for row in cursor.fetchall():
        book = Book(row[0], row[1], row[2], row[3])
        books.append(book)
    conn.close()
    return books

def add_book_to_db(db_path, book):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO books (title, author, year, isbn) VALUES books (?, ?, ?, ?)"
        (3, book.title, book.author, book.year, book.isbn)
    )
    conn.commit()
    conn.close()