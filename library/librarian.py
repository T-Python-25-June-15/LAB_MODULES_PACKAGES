def add_book(library : dict, title : str, author : str, isbn : str):
    if isbn in library:
        return "Already There"
    
    library[isbn] = {
        "title": title, 
        "author": author, 
        "available": True ,
        "isbn": isbn
        }
    return "Book Added"

def remove_book(library: dict, isbn: str):
    if isbn in library:
        del library[isbn]
        return "Book has been removed."
    else:
        return "Book not found. Cannot remove."


def check_out_book(library : dict, isbn : str):

    if isbn not in library:
        return "Not exist"
    
    if library[isbn]["available"]:
        library[isbn]["available"] = False
        return "You Take the book"
    
    return "Already Taken"


def return_book(library : dict, isbn : str):
    
    if isbn not in library:
        return "Not exist"
    
    
    library[isbn]["available"] = True
    return "You Returned The book"
    

def display_books(library: dict):
    if not library:
        print("The library is empty.")
        return
    
    print("\n--- Library Books ---")
    for isbn, book_info in library.items():
        if book_info["available"]:
            status = "Available"
        else:
            status = "Checked Out"
        print(f"Title: {book_info['title']}")
        print(f"Author: {book_info['author']}")
        print(f"ISBN: {isbn}")
        print(f"Status: {status}")
        print("------------------------")

    

