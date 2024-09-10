class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category
        self.available = True

    def borrow(self):
        self.available = False

    def return_book(self):
        self.available = True

    def __repr__(self) -> str:
        return self.title + ' by ' + self.author