def add_book(library:dict,title:str,author:str,isbn:str):
 
    if isbn in library:
        print("aleardy exists")
    else:
        library[isbn]= { 
                "title":title,
                "author":author,
                "available":True,
            }
                
        print("Added successfully.")

def remove_book(library:dict,isbn:str):
    if isbn in library:
        del library[isbn]
        print("Deleted book.")
    else:
        print("book not found")

def check_out_book(library:dict,isbn:str):
    if isbn in library:
           if library[isbn]["available"]==True:
            library[isbn]["available"]= False
            print("check out.")
           else:
            print("already checked out.")
    else:
        print("The book is not found.")

def return_book(library:dict,isbn:str):
    
    if isbn in library:
        if library[isbn]["available"]==False:
            library[isbn]["available"]= True
            print("Return done.")

        else:
            print("book available")
    else:
         print("The book is not found.")

def display_book(library:dict):
    for isbn,library2 in library.items():
        if library2["available"]== True:
            book_state= "available"
        else:
             book_state= "Checked Out"
        print(f"{library2["title"]} by {library2["author"]} (ISBN: {isbn} ) - {book_state} ")

