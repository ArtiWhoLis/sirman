class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title}, автор = {self.author}, год издания - {self.year}"


class User:
    def __init__(self, name: str, id: str, email: str):
        self.name = name
        self.membership_id = id
        self.email = email

    def __str__(self):
        return f"Имя: {self.name}, ID читателя: {self.membership_id}, Email: {self.email}"