
def add_book(library:dict, title:str, author:str, isbn:str):
    'Adds a new book to the library'
    if isbn in library:
        print("This book already exists!")
    else:
        library[isbn]= {"title":title, "author":author, "available": True}
        print(f"{isbn} - {title} was added successfuly!")
        
def remove_book(library:dict, isbn:str):
    'Removes a book from the library by its ISBN'
    if isbn in library:
        removed = library.pop(isbn)
        print(f"The book ({isbn} - {removed['title']}) has been deleted successfully!")
    else:
        print("Sorry but this book dosn't exists!")

def check_out_book(library:dict, isbn:str):
    'Marks a book as checked out'
    if isbn in library:
        library[isbn]["available"] = False
    else:
        print("Sorry but this book dosn't exists!")

def return_book(library:dict, isbn:str):
    'Marks a book as returned'
    if isbn in library:
        library[isbn]["available"] = True
    else:
        print("Sorry but this book dosn't exists!")

def display_books(library: dict):
    'Displays all books in the library'
    for key, value in library.items():
        availability = "Unknown"
        if  value['available'] == True:
            availability = "Available"
        else:
            availability = "Checked Out"
        print (f"{value['title']} by {value['author']} (ISBN: {key}) - {availability}")  