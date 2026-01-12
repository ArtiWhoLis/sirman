# Импортируем основные классы для удобного доступа
from .book import Book
from .user import User

# Определяем что будет доступно при from models import *
__all__ = ['Book']
_all__ = ['User']