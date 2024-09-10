from typing import Dict

from srp.book import Book
from ocp.search import BookSearch
from isp.notifier import EmailNotifier
from dip.loan_approval import BookAvailabilityHandler, UserEligibilityHandler, LoanLimitHandler
from srp.user import User
from utils.config_manager import ConfigurationManager
from utils.mediator import LibraryMediator

class LibraryFacade:
    def __init__(self):
        self.books = []
        self.users = []
        self.search = BookSearch()
        self.notifier = EmailNotifier()
        self.config_manager = ConfigurationManager()
        self.mediator = LibraryMediator()

        # Configuração do fluxo de aprovação de empréstimos
        self.approval_handler = BookAvailabilityHandler()
        self.approval_handler.set_next(UserEligibilityHandler()).set_next(LoanLimitHandler())

    def add_book(self, title: str, author: str, category: str):
        book = Book(title, author, category)
        self.books.append(book)

    def add_user(self, user: User):
        self.users.append(user)

    def borrow_book(self, user: User, book_title: str):
        books = self.search.search_by_title(self.books, book_title, True)
        if books:
            request: Dict[User, Book] = {'user': user, 'book': books[0]}
            result = self.approval_handler.handle(request)
            if result is None:
                books[0].borrow()
                user.borrow_book(books[0])
                self.notifier.notify(user, f"You have borrowed the book: {books[0]}")
                return "Book borrowed successfully"
            return result
        return f"Book '{book_title}' not found"

    def return_book(self, user: User, book_title: str):
        book = self.search.search_by_title(user.borrowed_books, book_title)
        if book:
            book[0].return_book()
            user.return_book(book[0])
            self.notifier.notify(user, f"You have returned the book: {book_title}")
            return "Book returned successfully"
        return f"Book '{book_title}' not found in user's borrowed books"