# include functions for managing books and patrons in a library system without using classes.
def add_book(library: dict, title: str, author: str, isbn: str):
    if isbn in library:
        print(f"ISBN {isbn} already exists.")
    else:
        library[isbn] = {
            'title': title,
            'author': author,
            'isbn': isbn,
            'available': True
        }
    
def remove_book(library: dict, isbn: str):
    if isbn in library: 
        del library[isbn]
    else:
        print(f"ISBN {isbn} does not exist in the library")

def check_out_book(library: dict, isbn: str):
    if isbn in library: 
        library[isbn]['available'] = False
    else:
        print(f"ISBN {isbn} not exist in the library")  

def return_book(library: dict, isbn: str):
    if isbn in library: 
        library[isbn]['available'] = True
    else:
        print(f"ISBN {isbn} not exist in the library")  

def display_books(library: dict):
    for element in library.values():
        if element['available']:
            status = "Available" 
        else:
            status ="Checked Out"
        print(f"{element['title']} by {element['author']}  (ISBN: {element['isbn']} - {status})")
