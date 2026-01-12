from src.models.book import Book

def test_book_borrow_true():
    '''Позитивный тест бронирования книги'''
    book = Book("Алиса в стране чудес", "Льюис Кэрролл", 1865,"242-252-6463-743")
    assert book.is_available == True
    assert book.borrow() == "Книга 'Алиса в стране чудес' выдана"
    assert book.is_available == False
    #assert book.borrow() == "Выдача книги 'Алиса в стране чудес' невозможна"

def test_book_return_true():
    book = Book("Колобок", "народ", 1865, "978-5-17-106077-0")
    book.borrow()  
    assert book.return_book() == "Книга 'Колобок' возвращена"
    assert book.return_book() == "Книга 'Колобок' уже доступна"


