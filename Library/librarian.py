

# I added this function to check if a isbn is in the library or not. 
def isExist(library:dict, isbn:str):
    return isbn in library.keys()


# This function to check if a book is available or not. 
def isAvailable(library:dict, isbn:str):
    return library[isbn]["available"]




def add_book(library:dict, title:str, author:str, isbn:str):

    book = {
        'title': title,
        'author': author,
        'available': True
    }
   
    if not isExist(library, isbn):
        library[isbn] = book
    else:
        print('ERROR: book already exist.')

    




def remove_book(library:dict, isbn:str):
    if isExist(library, isbn):
        del library[isbn]
    else:
        print("ERROR: The ISBN is not exist.")





def check_out_book(library:dict, isbn:str):
    if isExist(library, isbn):
        if isAvailable(library, isbn):
            library[isbn]['available'] = False
        else:
            print(f"ERROR: The book: {library[isbn]['title']} is not Available.")

    else:
        print(f"ERROR: The ISBN: {isbn} is not exist.")
    


def return_book(library:dict, isbn:str):
    if isExist(library, isbn):
            library[isbn]['available'] = True

    else:
        print(f"ERROR: The ISBN: {isbn} is not exist.")


def display_books(library:str):
    keys = list(library.keys())
     
    for isbn in keys:
        print(f"{library[isbn]['title']} by {library[isbn]['author']} (ISBN: {isbn}) - {'Available' if library[isbn]['available'] else 'Checked Out'}")
    








