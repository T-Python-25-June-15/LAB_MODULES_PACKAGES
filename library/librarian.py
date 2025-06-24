def add_book(library: dict, title: str, author: str, isbn: str):
    for book in library:
        if library[book]["isbn"] == isbn:
            print("This book is already exists with the same ISBN, try anthore ISBN ")
            return

    new_library = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "available": True
    }

    print("Book added successfully.")
    library.update({isbn: new_library})
                      

                      




def remove_book(library:dict, isbn:str):
    for book in library:
        if library[book]["isbn"]==isbn:
            del library[book]
            print(f"Book removed successfully.{book}")
            return

        else:
            print("This book with this ISBN does not exist, try anthore ISBN")








def check_out_book(library:dict, isbn:str):
    for book in library:
        if library[book]["isbn"] == isbn:
            if library[book]["available"]==False:
                print("Book is not available for checkout.")
            else:
                library[book]["available"] = False
                print(f"Book has been checked out successfully. {book}")
            return
    print("This book with this ISBN does not exist. Try another ISBN.")
            







def return_book(library:dict, isbn:str):
    for book in library:
        if library[book]["isbn"] == isbn:
            if library[book]["available"]==True:
                print("The book is already available.")
            else:
                library[book]["available"] = True
                print(f"Book has been returned successfully.{book}")
            return
    print("This book with this ISBN does not exist. Try another ISBN.")




def display_books(library: dict):
    for index, book_key in enumerate(library, start=1):
        book = library[book_key]
        availability = "Available" if book["available"] else "Checked Out"
        print(f"{index}. {book['title']} by {book['author']} (ISBN: {book['isbn']}) - {availability}")
    print()
