from library.librarian import *

print("Welcome to our library system!")
while True :
    print("-"*50)
    print("a.To add a book to our library")
    print("b.To remove a book from our library")
    print("c.To checkout/borrow a book from our library")
    print("d.To return a book to our library")
    print("e.To show all books")
    print("f.exit")
    choice = input("please enter your choice from the menu above:")

    if choice == "a":
        print("-"*50)
        title = input("Please enter the title of the book: ")
        author = input("Please enter the author name: ")
        isban = input("Please enter the ISBN: ")
        add_book(library,title,author,isban)

    elif choice == "b":
        print("-"*50)
        display_books(library)
        isban = input("Please enter the ISBN to remove the book: ")
        remove_book(library,isban)   
        print("The updated Library is shown below:")
        display_books(library)

    elif choice == "c":
        print("-"*50)
        isban = input("Please enter the ISBN to borrow the book: ")
        check_out_book(library, isban)
        
    elif choice == "d":
        print("-"*50)
        isban = input("Please enter the ISBN to return the book: ")
        return_book(library, isban)
    elif choice == "e":
        print("-"*50)
        display_books(library)
        print("-"*50)
    
    else:
        break