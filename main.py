"""
Модуль для демонстрации работы с классами Book и User.

В этом модуле создаются экземпляры классов Book и User,
демонстрируется их использование и выводится информация в консоль.

Modules:
    logging: Для отслеживания работы программы и вывода сообщений отладочного уровня.
    src.models.book: Содержит определение класса Book.
    src.models.user: Содержит определение класса User.
"""

from src.models.book import Book
from src.models.user import User
import logging

logger = logging.getLogger()
logger.debug(f'Логгер {__name__} создан')


def main():
    """Главная функция модуля.

    Создаёт экземпляры книг и пользователя, затем выводит информацию о них.

    Raises:
        ImportError: Если модули Book или User недоступны.
    """

    title1 = "Гарри Поттер и Философский камень"
    title2 = "Капитанская дочка"
    author1 = "Дж.К.Роулинг"
    author2 = "А.С.Пушкин"
    isbn = "978-3-16-148410-0"

    book1 = Book(title1, author1, 1997, isbn)
    print(book1.get_info())

    book2 = Book(title2, author2, 1999, isbn)
    print(book2.get_info())

    user = User("Иван", "М", "+7 982-838-18-48", "'Золушка', 'Золотая рыбка'")
    print(user.get_info())


if __name__ == "__main__":
    main()