from typing import Dict

from srp.book import Book
from srp.user import User

class LoanApprovalHandler:
    next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return None

class BookAvailabilityHandler(LoanApprovalHandler):
    def handle(self, request: Dict[User, Book]):
        if request['book'].available:
            return super().handle(request)
        return "Book not available"

class UserEligibilityHandler(LoanApprovalHandler):
    def handle(self, request: Dict[User, Book]):
        if request['user'].is_eligible():
            return super().handle(request)
        return "User not eligible"

class LoanLimitHandler(LoanApprovalHandler):
    def handle(self, request: Dict[User, Book]):
        if len(request['user'].borrowed_books) < request['user'].loan_limit:
            return super().handle(request)
        return "Loan limit reached"