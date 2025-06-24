


def add_book (library , title , author , isbn):
    if isbn in library:
        print("The book is exist in the library.")
    else:
        library[isbn] = {
            "title" : title,
            "author" : author,
            "isbn" : isbn,
            "available" : True
        }
        print(f"Book {title} has added to the library.")



def remove_book(library , isbn):
    if isbn in library:
        del library[isbn]
        print(f"The book deleted successfully.")
    else:
        print("This book isn't in the library!")



def check_out_book(library, isbn):
    if isbn in library:
        if library[isbn]["available"]:
            library[isbn]["available"] = False
            print("Book checked out successfully.")
        else:
            print("Book isn't available right now.")
    else:
        print("Book isn't in this library.")



def return_book(library, isbn):
    if isbn in library:
        library[isbn]["available"] = True
        print("The book has returned successfully, thanks.")
    else:
        print("This book isn't ours.")


def display_books(library):
    for isbn, book in library.items():
        title = book["title"]
        author = book["author"]
        available = book["available"]
        if available == True: 
            available = "Available"
        else:
            available = "Checked Out"

        print(f"{title} by {author} (ISBN: {isbn}) - {available}")