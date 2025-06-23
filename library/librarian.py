def add_book(library, title, author, isbn):
    if isbn in library:
        print("book exist")
    else:
        library [isbn]={
            "title" : title,
            "author" : author,
            "isbn" : isbn,
            "available" : True

        }
        print(f"book added {title}")

def remove_book(library, isbn):
    if isbn in library:
        del library [isbn]
        print ("book removed")
    else:
        print("book not in database")

def check_out_book(library , isbn):
    if isbn in library:
        library[isbn]["available"]=False
        print(f"book checked out {isbn}")
    else:
        print("book not in database")

def return_book(library, isbn):
    if isbn in library:
        library[isbn]["available"]=True
        print(f"book returned {isbn}")
    else:
        print("book not in database")

def display_books(library):
    for book in library.values():
        print(book ["title"], "by", book["author"])
    print()





