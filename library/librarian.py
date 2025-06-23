library = {

}

def add_book(library , title : str , author : str , isbn : str):
    if isbn in library:
      print("The book is already available.")
       
    else:
       new_book = {
             "title" : title ,
             "author" : author,
             "ISBN"  : isbn ,
             "available" : True
         }

       library[isbn] = new_book
       print(f"added {title} in the library")


def remove_book(library , isbn : str) :
   
      if isbn in library :
         library.pop(isbn)
         print(f"the book removed")
      else:
        print("the isbn dosen't exist ") 

def check_out_book(library , isbn : str) :
   
   if isbn in library:
        if library[isbn]["available"]:
          library[isbn]["available"] = False
          print("the book checked out")
        else:
          print("the book is already checked out")
   else:
      print("book not found ")
    

def return_book(library , isbn : str):
   if isbn in library:
        library[isbn]["available"] = True
        print(f"You have returned '{library[isbn]['title']}'.")
   else:
        print("Book not found in the library.")

def display_books(library):
    if not library:
        print("The library is empty.")
    else:
        for isbn, book in library.items():
            if book["available"] == True:
                status = "Available"
            else:
                status = "Checked Out"
            print(f"{book['title']} by {book['author']} (ISBN: {isbn}) - {status}")
            