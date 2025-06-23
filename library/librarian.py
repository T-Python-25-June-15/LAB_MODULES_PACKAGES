#------------------------------------------------------------# Add Book

def add_book(library, title, author, isbn):
    library[isbn] = {"title": title,"author": author,"isbn": isbn,"available": True}
    
#------------------------------------------------------------# Remove Book

def remove_book(library, isbn):
    if isbn in library:
        del library[isbn]
    else:
        print("Book Not found in the library.")
#------------------------------------------------------------# Check Out Book
def check_out_book(library, isbn):
    if isbn in library:
        library[isbn]["available"] = False
    else:
        print("Book not found in the library.")
#------------------------------------------------------------# Return Book

def return_book(library, isbn):
    if isbn in library:
        library[isbn]["available"] = True
    else:
        print("Book not found in the library.")
#------------------------------------------------------------# Display Books

def display_books(library):
    for book in library.values():
        status = "Available" if book["available"] else "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status}")
    print()
