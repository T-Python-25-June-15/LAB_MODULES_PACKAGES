

def add_book(library: dict, title: str, author: str, isbn: str) -> None:
    if isbn in library:
        print(f"Sorry, this book '{title}' is already in the library.")
    else:
        library[isbn] = {'title': title, 'author': author, 'available': True}
        print(f"Added book with ISBN: {isbn} successfully.")


def remove_book(library: dict, isbn: str) -> None:
    if isbn in library:
        library.pop(isbn)
        print("Successfully removed.")
    else:
        print(f"This book with ISBN {isbn} is not in the library.")


def check_out_book(library: str, isbn: str) -> None:
    if isbn in library:      
        if library[isbn]['available'] == True:      
            library[isbn]['available'] = False
            print(f"Now the book with ISBN {isbn} is checked out.")
        else: 
            print(f"Book with ISBN: {isbn} is already checked out.")
    else:
        print(f"This book with ISBN {isbn} does not exist.")


def return_book(library: str, isbn: str) -> None:
    if isbn in library:
        if library[isbn]['available'] == False:
            library[isbn]['available'] = True
        else:
            print("This book is already not checked out.")
    else:
        print("Sorry, this book does not exist.")


def display(library: dict) -> None:
    for isbn in library:
        if library[isbn]['available'] == True:
            print(f"{library[isbn]['title']} by {library[isbn]['author']} (ISBN: {isbn}) - Available")
        else:
            print(f"{library[isbn]['title']} by {library[isbn]['author']} (ISBN: {isbn}) - Checked Out")
