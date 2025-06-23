

def add_book(library:dict, title:str, author:str, isbn:str):
    available = True
    if isbn in library:
        print(f"{library} - Checked Out")
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
    else:
        library[isbn]["available"] = True
        print(f"The book with this ISBN : {isbn} is now returned")

def display_books(library:dict):
    for isbn in library:
        if library[isbn]["available"] == True:
            print(f"{library[isbn]["title"]} by {library[isbn]["author"]} (ISBN: {library[isbn]["isbn"]}) - Available")
        else:
            print(f"{library[isbn]["title"]} by {library[isbn]["author"]} (ISBN: {library[isbn]["isbn"]}) - Checkout")
'''
add_book(library,"The Catcher in the Rye","J.D. Salinger", "9780316769174")
add_book(library,"To Kill a Mockingbird","Harper Lee","9780446310789")
add_book(library,"1984","George Orwell","9780451524935")
remove_book(library, "9780451524935")
check_out_book(library,"9780316769174")
check_out_book(library,"9780446310789")
return_book(library,"9780446310789")
display_books(library)
'''

