
def add_book(library, title:str, author:str, isbn:str ):
    if isbn in library:
        print("the book is already exist")
    else:
         library[isbn]= {
         "title" : title,
         "author": author,
         "isbn" : isbn,
         "available": True
    }
    print(f"Book {title} by {author} added to the library")

def remove_book(library, isbn:str):
    if isbn in library:
        del library[isbn]
        print("The book was successfully deleted")
    else:
        print("The ISBN is not correct")

def check_out_book(library, isbn:str):
    if isbn not in library:
        print("The ISBN dose not exist")
    else: 
        library[isbn]["available"] == False
        print(f"book {library[isbn]["title"]} checked out successfully")

def return_book(library, isbn:str):
    if isbn == library["isbn"]:
        library["available"] == True
        print("The availability of the book is set to True")
    else: 
        print("The ISBN dose not exist")

def display_books(library):
    for isbn, book in library.items():
        if book['available']:
            status = "Available"
        else:
            status = "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status}")