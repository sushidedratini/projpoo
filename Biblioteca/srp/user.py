import uuid


class User:
    def __init__(self, name):
        self.user_id = uuid.uuid4()
        self.name = name
        self.borrowed_books = []
        self.loan_limit = 5

    def borrow_book(self, book) -> None:
        self.borrowed_books.append(book)
        self.loan_limit -= 1

    def return_book(self, book) -> None:
        self.borrowed_books.remove(book)
        self.loan_limit += 1

    def is_eligible(self) -> bool:
        if self.loan_limit == 0:
            return False
        return True

    def __repr__(self) -> str:
        return f"ID: {self.user_id} | Name: {self.name} | Borrowed Books: {self.borrowed_books}"
