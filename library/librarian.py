def add_book(books, title,author, isbn):
    if isbn in books:
        print("available")
    else:
        books[isbn] = {
            "title":title,
            "author":author,
            "ISBN":isbn,
            "available":True,}
def delete(books,isbn):
    if isbn in books:
        del books[isbn]
    else:

        print("not available")

def check_out_book(books, isbn):
    if isbn in books:
        if books[isbn]["available"]:
            books[isbn]["available"]=False
        else:
            print("not available")
    else:
        print("not exist")

def return_book(books,isbn):
    if isbn in books:
        books[isbn]["available"] = True
    else:
        print("not available")

def display_book(books):
    for isbn , book in books.items():
          if book ["available"]:
              statu="available"
          else:
              statu="not avaliable"
          print(f"{book['title']} by {book['author']} (ISBN:{isbn})- {statu}")
