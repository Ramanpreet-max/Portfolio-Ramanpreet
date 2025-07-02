# File: /library-management/library-management/src/main.py

class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.controller = LibraryController(self.books)

    def main_loop(self):
        while True:
            print("\nLibrary Management System")
            print("1. Add Book")
            print("2. Remove Book")
            print("3. List Books")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.remove_book()
            elif choice == '3':
                self.list_books()
            elif choice == '4':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter book ISBN: ")
        self.controller.add_book(title, author, isbn)
        print("Book added successfully.")

    def remove_book(self):
        isbn = input("Enter book ISBN to remove: ")
        if self.controller.remove_book(isbn):
            print("Book removed successfully.")
        else:
            print("Book not found.")

    def list_books(self):
        books = self.controller.list_books()
        if books:
            print("Books in the library:")
            for book in books:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
        else:
            print("No books available in the library.")

if __name__ == "__main__":
    from controllers.library_controller import LibraryController
    library_system = LibraryManagementSystem()
    library_system.main_loop()