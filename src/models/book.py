import src.utils.logger
import logging


class Book:
    """Класс, представляющий книгу в библиотечной системе.

    Класс отвечает за хранение информации о книге и управление её состоянием — доступна ли она для выдачи.
    При создании экземпляра настраивает базовую систему логирования, позволяющую отслеживать действия с книгами.

    Attributes:
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания книги.
        isbn (str): Международный стандартный книжный номер.
        is_available (bool): Флаг доступности книги для выдачи.

    """

    def __init__(self, title: str, author: str, year: int, isbn: str):
        """Инициализирует экземпляр книги и настраивает логирование.

        Args:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.
            isbn (str): ISBN книги.

        Raises:
            ValueError: Если год издания некорректен (например, в будущем).
        """
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.is_available = True

        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename='library.log'
        )

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter('%(asctime)s -  %(message)s'))
        logging.getLogger().addHandler(console_handler)

        logger = logging.getLogger(__name__)
        logger.debug(f"{self.title}, автор - {self.author}, год издания - {self.year}")
        logger.info(f"{self.title}, автор - {self.author}, год издания - {self.year}")

    def get_info(self) -> str:
        """Возвращает краткую информацию о книге.

        Returns:
            str: Строка с названием, автором и годом издания книги.
        """
        return f"{self.title}, автор - {self.author}, год издания - {self.year}"

    def borrow(self) -> str:
        """
        Пример
        >>> book = Book("Книга", "Автор", "Год издания")
        >>> book.borrow()
        Книга выдана
        
        Выдаёт книгу пользователю, если она доступна.

        Изменяет состояние книги — делает её недоступной для повторной выдачи до возврата.

        Returns:
            str: Сообщение о результате операции (успешная выдача или невозможность выдать книгу).
        """
        if self.is_available:
            self.is_available = False
            return f"Книга '{self.title}' выдана"
        else:
            return f"Выдача книги '{self.title}' невозможна"

    def return_book(self) -> str:
        """Принимает возвращённую книгу и делает её снова доступной.

        Returns:
            str: Сообщение о результате возврата книги.
        """
        if not self.is_available:
            self.is_available = True
            return f"Книга '{self.title}' возвращена"
        else:
            return f"Книга '{self.title}' уже доступна"


class EBook(Book):
    """Класс, представляющий электронную книгу.

    Наследуется от базового класса Book и добавляет атрибут формата файла.

    Attributes:
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания книги.
        isbn (str): ISBN книги.
        format (str): Формат электронного файла (например, 'pdf', 'epub').

    """

    def __init__(self, title: str, author: str, year: int, format: str, isbn: str):
        """Инициализирует экземпляр электронной книги.

        Args:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.
            format (str): Формат файла электронной книги.
            isbn (str): ISBN книги.
        """
        super().__init__(title, author, year, isbn)
        self.format = format

    def get_info(self) -> str:
        """Возвращает информацию об электронной книге, включая формат файла.

        Returns:
            str: Строка с названием, автором, годом издания и форматом файла.
        """
        return f"{self.title}, автор - {self.author}, год издания - {self.year}, формат - {self.format}"