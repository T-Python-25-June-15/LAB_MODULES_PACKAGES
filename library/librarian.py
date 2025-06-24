#Luluh Almogbil
'''
3. Create a new file named `librarian.py` inside the `library` folder. In this file, define the following functions:

  a - `add_book(library, title, author, isbn)` - takes a dictionary (library), a title (string), an author (string), and an ISBN (string) as input, 
   and adds a new book to the library as a dictionary with the keys 'title', 'author', 'isbn', and 'available'. 
   The 'available' key should have a boolean value, initially set to True. If the ISBN already exists in the library, print an appropriate message.

  b - `remove_book(library, isbn)` - takes a dictionary (library) and an ISBN (string) as input, and removes the book with the given ISBN from the library. If the ISBN does not exist in the library, print an appropriate message.
  c - `check_out_book(library, isbn)` - takes a dictionary (library) and an ISBN (string) as input, and sets the 'available' key of the book with the given ISBN to False. If the ISBN does not exist in the library or the book is not available, print an appropriate message.
  d - `return_book(library, isbn)` - takes a dictionary (library) and an ISBN (string) as input, and sets the 'available' key of the book with the given ISBN to True. If the ISBN does not exist in the library, print an appropriate message.
  e - `display_books(library)` - takes a dictionary (library) as input and prints all the books in the library in a formatted way.

4. Write a script named `main.py` in your working directory (outside the `library` folder) that imports and uses the `librarian` module from the `library` package to manage a simple library system.

5- use the function from librarian to add books, remove book, checout a book, and display books .

### A sample output should look like this when you run main.py
```
The Catcher in the Rye by J.D. Salinger (ISBN: 9780316769174) - Available
To Kill a Mockingbird by Harper Lee (ISBN: 9780446310789) - Available
1984 by George Orwell (ISBN: 9780451524935) - Available

The Catcher in the Rye by J.D. Salinger (ISBN: 9780316769174) - Checked Out
To Kill a Mockingbird by Harper Lee (ISBN: 9780446310789) - Available
1984 by George Orwell (ISBN: 9780451524935) - Available

The Catcher in the Rye by J.D. Salinger (ISBN: 9780316769174) - Available
To Kill a Mockingbird by Harper Lee (ISBN: 9780446310789) - Available
1984 by George Orwell (ISBN: 9780451524935) - Available

'''

#myfunctions
#a add book
library = {}
def add_book(library:dict, title:str, author:str, isban:str):
    if isban in library:
        print(f"{isban} already exists in the library")
    else:
        library[isban] = {"title":title,
                   "author":author,
                   "isban":isban,
                   "available": True
                   }
        print("Book added to the library successfully") 
        
#b remove book
def remove_book(library, isban):
    if isban in library:# remove it
        del library[isban]
        print("Book has been removed successfully")
    else:
        print("ISBAN doesnt exist")
        
        
# c borrow a book /ckeckout and check if book availble or not 
def check_out_book(library, isban):
    if isban in library :
        if library[isban]['available'] == True:# if the book is there and its available
            library[isban]['available'] = False#to assign another value
            
        else:
            print("The book is already borrowed/checked out")
        
    else:
        print("ISBAN doesnt exist")
        
#e return a book
def return_book(library, isban):
    if isban in library :
        if library[isban]['available'] == False:# if the book is there but checked out
            library[isban]['available'] = True #give the book back to the library
            print("the book is retuned.Thank you")
        else:
            print("The book is already available")   
    else:
        print("ISBAN doesnt exist  ")
        
        
# e show all books
def display_books(library):
    if not library:
        print("The library is empty for now")
    else:
        for i,(isban,book) in enumerate(library.items(),start=1):#start from index 1
            print(f"{i}. {book['title']} by {book['author']} (ISBN:{isban}) - {'Available' if book['available'] else 'Checked Out'}")
       

  
        
# print("Welcome to our library system!")
# while True :
#     print("a.To add a book to our library")
#     print("b.To remove a book from our library")
#     print("c.To checkout/borrow a book from our library")
#     print("d.To return a book to our library")
#     print("e.To show all books")
#     print("f.exit")
#     choice = input("please enter your choice from the menu above:")

#     if choice == "a":
#         print("-"*50)
#         title = input("Please enter the title of the book: ")
#         author = input("Please enter the author name: ")
#         isban = input("Please enter the ISBN: ")
#         add_book(library,title,author,isban)

#     elif choice == "b":
#         print("-"*50)
#         display_books(library)
#         isban = input("Please enter the ISBN to remove the book: ")
#         remove_book(library,isban)   
#         print("The updated Library is shown below:")
#         display_books(library)

#     elif choice == "c":
#         print("-"*50)
#         isban = input("Please enter the ISBN to borrow the book: ")
#         check_out_book(library, isban)
        
#     elif choice == "d":
#         print("-"*50)
#         isban = input("Please enter the ISBN to return the book: ")
#         return_book(library, isban)
#     elif choice == "e":
#         print("-"*50)
#         display_books(library)
#         print("-"*50)
    
#     else:
#         break


    
    
