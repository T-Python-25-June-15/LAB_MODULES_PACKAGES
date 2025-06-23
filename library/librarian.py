
def add_book(library:dict, title:str, auther:str, isbn:str):
    for book in library.keys():
        if library[book]["isbn"] == isbn:
            print("the book is already exixst!")
            return library
    
    new_book = {
        "title": title,
        "auther": auther,
        "isbn": isbn,
        "available": True
    }
    
    library.update([[isbn, new_book]])
    
    return library


def remove_book(library:dict, isbn:str):
    for book in library.keys():
        if library[book]["isbn"] == isbn:
            del library[book]
            return library
    
    print("The ISBN you entered is incorrect.")
    return library

def check_out_book(library:dict, isbn:str):
    for book in library.keys(): # checkk the isbn first
        if library[book]["isbn"] == isbn:
            if library[book]["available"] == True:
                library[book]["available"] = False
                return library
            else:
                print("The book is already reserved.")
                return library
    
    print("The ISBN you entered is incorrect.")
    return library

def return_book(library:dict, isbn:str):
    for book in library.keys():
        if library[book]["isbn"] == isbn:
            library[book]["available"] = True
            return library
    
    print("The ISBN you entered is incorrect.")
    return library

def display_books(library:dict):
    for book in library:
        r = ""
        if library[book]["available"]: r = "Available"
        else: r = "Checked Out"
        print(f"{library[book]["title"]} by {library[book]["auther"]} (ISBN: {library[book]["isbn"]}) - {r}")
        
    print()




