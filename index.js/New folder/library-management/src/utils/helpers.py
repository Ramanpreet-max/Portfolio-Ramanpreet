def validate_isbn(isbn):
    if len(isbn) == 10 or len(isbn) == 13:
        return True
    return False

def format_book_details(book):
    return f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}"