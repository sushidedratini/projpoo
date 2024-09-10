class LibraryMediator:
    def __init__(self):
        self.facade = None

    def set_facade(self, facade):
        self.facade = facade

    def notify(self, event: str, data):
        if event == "borrow_book":
            return self.facade.borrow_book(data['user'], data['book_title'])
        elif event == "return_book":
            return self.facade.return_book(data['user'], data['book_title'])
        elif event == "add_book":
            self.facade.add_book(data['title'], data['author'], data['category'])
        elif event == "add_user":
            self.facade.add_user(data['user'])