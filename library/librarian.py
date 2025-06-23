
def add_book(library, title, author, isbn):
    if isbn in library:
        print("Book already exist")
    else:
        library[isbn] ={
            "title":title,
            "author":author,
            "isbn":isbn,
            "availabilty":True,
        }

def remove_book(library, isbn):
    if isbn in library:
        del library[isbn]
        print("The book removed!")
    else:
        print("There is no book with this isbn")


def check_out_book(library, isbn):
    if isbn in library or library[isbn]["availabilty"] == True:
        library[isbn]["availabilty"] = False

def return_book(library, isbn):
    library[isbn]["availabilty"] = True

def display_books(library):
    for books in library:
        shortway = library[books]
        if shortway["availabilty"] == False:
            availB = "Not Available"
        elif shortway["availabilty"] == True:
            availB = "Available"
        print(f"""
                ----------------------
                {shortway["title"]} by {shortway["author"]} (ISBN: {shortway['isbn']}) - {availB}
                ----------------------
                """)
        