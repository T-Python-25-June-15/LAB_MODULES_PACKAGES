

def add_book(library:dict, title:str, author:str, isbn:str):
    available = True
    if isbn in library:
        print(f"This Book is already in the library!")
    else:
        library[isbn] = {"title":title, "author":author, "isbn":isbn, "available":available}
        print(f"You added a new book: {title} by {author} (ISBN: {isbn}) - Available")

def remove_book(library:dict, isbn:str):
    if isbn not in library:
        print("There is no book with this ISBN")
    else:
        del library[isbn]
        print(f"The book with ISBN: {isbn} has been removed")

def check_out_book(library:dict, isbn:str):

    if isbn not in library:
        print("There isn't any book with this ISBN")
    elif library[isbn]["available"] == False:
        print("The book with this ISBN has been checked out")
    else:
        library[isbn]["available"] = False
        print(f"The book with this ISBN : {isbn} is now checkout")

def return_book(library:dict, isbn:str):
    if isbn not in library:
        print(f"There was no book with this ISBN: {isbn} for you to return it")
    elif library[isbn]["available"] == True:
        print(f"This book with this ISBN: {isbn} can't be returned because it already in the library!")
    else:
        library[isbn]["available"] = True
        print(f"The book with this ISBN : {isbn} is now returned")

def display_books(library:dict):
    for isbn in library:
        if library[isbn]["available"] == True:
            print(f"{library[isbn]["title"]} by {library[isbn]["author"]} (ISBN: {library[isbn]["isbn"]}) - Available")
        else:
            print(f"{library[isbn]["title"]} by {library[isbn]["author"]} (ISBN: {library[isbn]["isbn"]}) - Checkout")


