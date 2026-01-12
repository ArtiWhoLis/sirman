from src.models.book import Book
from src.models.user import User

import src.utils.logger
import logging

logger = logging.getLogger()
logger.debug(f'Логгер {__name__} создан')


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
