class User:
	def __init__(self, name: str, gender: str, phone: int, borrow_history: str):
		self.name = name
		self.gender = gender
		self.phone = phone
		self.borrow_history = borrow_history 
	def get_info(self) -> str:
	    return f"{self.name}, пол - {self.gender}, телефон - {self.phone}, История книг - {self.borrow_history}"
		
