class Book:
	"""
	Класс отвечающий за книги в библиотеке.
	Подробное описание класса, что он делает, за что отвечает, какие основные функции выполняет.

	Attributes:
		title (str): Название книги.
		author (str): Автор книги.
		year (int): Год публикации.
		isbn (str): Уникальный код.
	"""

	def __init__(self, title: str, author: str, year: int, isbn: str):
		self.title = title
		self.author = author
		self.year = year
		self.isbn = isbn 
		self.is_available = True

	def __str__(self) -> str:
		return f"{self.title}, автор - {self.author}, год издания - {self.year}"
	
	def borrow(self) -> str:
		"""
		Метод выдачи книги.

		При вызове метода со свободной книгой меняет её статус на "Занято" и возвращает сообщение,
		если книга уже была занята — сообщает об невозможности выдачи.
		"""
		if self.is_available:
			self.is_available = False
			return f"Книга '{self.title}' выдана"
		else:
			return f"Выдача книги '{self.title}' невозможна — уже занята"
	
	def return_book(self) -> str:
		"""
		Метод возврата книги.
		
		Если книга была выдана — возвращает её в доступное состояние,
		если уже доступна — сообщает об этом.
		"""
		if not self.is_available:
			self.is_available = True
			return f"Книга '{self.title}' возвращена"
		else:
			return f"Книга '{self.title}' уже доступна"
		
		
class EBook(Book):
	"""
	Класс для электронных книг. Наследует основные свойства от Book
	и добавляет атрибут формата файла.
	"""

	def __init__(self, title: str, author: str, year: int, format: str, isbn: str):
		super().__init__(title, author, year, isbn)
		self.format = format

	def get_info(self) -> str:
		"""Возвращает краткие сведения об электронной книге."""
		return f"{self.title}, автор - {self.author}, год издания - {self.year}, формат - {self.format}"