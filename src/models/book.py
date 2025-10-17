class book:
    def __init__(self, title: str, author:str, year: int, pages: int, icbn: str):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.icbn = icbn

    def __str__(self) -> str:
        return f"{self.title}, Автор - {self.author} - {self.year}, страниц - {self.pages}, ICBN - {self.icbn}"


