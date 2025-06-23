
def add_book(library, title, author, isbn):

    library.append({
        'title': title,
        'author': author,
        'isbn': isbn,
        'available': (isbn != None)
    })
    status = "Available" if isbn else "Checked out"
    print(f"{title} book by {author}, and isbn : {isbn}, status {status} added to the library.")

def remove_book(library, isbn):
    isFound = False
    for book in library:
        if book['isbn'] == isbn:
            isFound = True
            print(f"book with isbn {isbn} removed")
            library.remove(book)
            break
    if isFound == False:
        print(f"book with isbn {isbn} not found")
    

def check_out_book(library, isbn):
    isFound = False
    for book in library:
        if book['isbn'] == isbn:
            isFound = True
            if book['available'] == True:
                book['available'] = False
                print(f"{book['title']} book isbn {isbn} now checked out")
                break
    if isFound == False:
        print(f"book with isbn {isbn} not found")


def return_book(library, isbn):
    isFound = False
    for book in library:
        if book['isbn'] == isbn:
            isFound = True
            if not book['available']:
                book['available'] = True
                print(f"{book['title']} book with isbn {isbn} now avaliable")
                break
    if isFound == False:
        print(f"book with isbn {isbn} not found")

def display_books(library):
    if not library:
        print("no books in the library")
        return
    print("books in the library:")
    for book in library:
        status = "Available" if book['available'] else "Checked out"
        print(f"{book['title']}. {book['author']} (ISBN: {book['isbn']}) - {status}")