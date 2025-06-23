#wasan alqahtani

#librarian file in libraray pacakge
def add_book(library:dict, title:str, author:str, isbn:str):
    '''takes a dictionary (library), a title , an author , and an ISBN  as argument
    , and adds a new book to the library as a dictionary '''
    if isbn in library:
        print("The ISBN of this book is already exists")
    else:
        library[isbn] = {
              'title':title, 
              'author':author, 
              'available':True
                }
        print("book added sucessfully")

def remove_book(library:dict, isbn:str):
    '''takes a dictionary  and an ISBN , and removes the book with 
    the given ISBN from the library'''
    #check if the this isbn exists or not
    if isbn in library:
        del library[isbn]
    else:
        print("The ISBN of this book is not exists")

def check_out_book(library:dict, isbn:str):
    '''takes a dictionary  and an ISBN and sets the 'available' key 
    of the book with the given ISBN to False'''
    #check if the this isbn exists or not and if its already checked out
    if (isbn in library) and (library[isbn]["available"]):
        #check if this isbn is already chekedout 
        library[isbn]["available"] = False
        print("this book has been checked out")
    
    else:
        print("This book or this ISBN dosent exists")

def return_book(library:dict, isbn:str):
    '''takes a dictionary (library) and an ISBN , 
    and sets the 'available' key of the book with the given ISBN to True.'''
    #check if the this isbn exists or not
    if isbn in library:
        library[isbn]["available"] = True
        print("this book has been retuned")
    else:
        print("The ISBN of this book is not exists")

def display_books(library:dict):
    '''this methos take dictionary and print all books'''
    for isbn, book in library.items():
        title = book["title"]
        author = book["author"]
        available = book["available"]
        if available == True: 
            available = "Available"
        else:
            available = "Checked Out"
            
        print(f"{title} by {author} (ISBN: {isbn}) - {available}")

    