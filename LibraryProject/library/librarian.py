def add_book(library, title, author, isbn):
    if isbn in library:
        print("Book already exists.")
    else:
        library[isbn] = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "available": True
        }

def remove_book(library, isbn):
    if isbn in library:
        del library[isbn]
        print("Book removed.")
    else:
        print("Book not found.")

def check_out_book(library, isbn):
    if isbn in library:
        if library[isbn]["available"] == True:
            library[isbn]["available"] = False
            print("Book checked out.")
        else:
            print("Book is already checked out.")
    else:
        print("Book not found.")

def return_book(library, isbn):
    if isbn in library:
        library[isbn]["available"] = True
        print("Book returned.")
    else:
        print("Book not found.")

def display_books(library):
    for book in library.values():
        if book["available"] == True:
            status = "Available"
        else:
            status = "Checked Out"
        print(book["title"], "by", book["author"], "(ISBN:", book["isbn"] + ")", "-", status)
