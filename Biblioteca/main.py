from utils.mediator import LibraryMediator
from lsp.user_types import StudentUser
from facade.library_facade import LibraryFacade

'''
    Eduardo Augusto Saito - RA: 140524
    Wallace dos Santos Costa - RA: 142548
'''
def main() -> None:
    library = LibraryFacade()

    mediator = LibraryMediator()
    mediator.set_facade(library)

    student = StudentUser(name="Eduardo", student_id="S123")
    olderStudent = StudentUser(name="Wallace", student_id="321")

    mediator.notify("add_user", {'user': student})
    mediator.notify("add_user", {'user': olderStudent})
    mediator.notify("add_book", {'title': "Python Programming",
                    'author': "John Smith", 'category': "Programming"})

    print(mediator.notify("borrow_book", {
          'user': student, 'book_title': "Lord of the Rings"}))
    print(mediator.notify("return_book", {
          'user': student, 'book_title': "Python Programming"}))
    print(mediator.notify("return_book", {
          'user': student, 'book_title': "Lord of the Rings"}))
    print(mediator.notify("borrow_book", {
          'user': olderStudent, 'book_title': "Battle Brothers"}))
    print(mediator.notify("borrow_book", {
          'user': olderStudent, 'book_title': 'As Aventuras do Wallace'}))


if __name__ == "__main__":
    main()
