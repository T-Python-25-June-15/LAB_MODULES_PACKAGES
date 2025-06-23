from library.librarian import *
library = {}
add_book(library,"The Catcher in the Rye","J.D. Salinger", "9780316769174")
add_book(library,"To Kill a Mockingbird","Harper Lee","9780446310789")
add_book(library,"1984","George Orwell","9780451524935")
remove_book(library, "9780451524935")
check_out_book(library,"9780316769174")
check_out_book(library,"9780446310789")
return_book(library,"9780446310789")
display_books(library)

print("-"*20)
print("This part down is bonus i felt like it")
print()
print("Welcome to our library")
user_choice = input("Please choose what you want to do: \n 1)add a new book to the library \n 2)remove a book from the library \n 3)Checkout a book \n 4)Return a book \n 5)Display all books \n To exit type 'exit': ")
while user_choice.lower() != "exit":
    if user_choice == "1":
        print()
        print("-"*15)
        user_book_title = input("Please enter the book title: ")
        if user_book_title == "":
            print("You need to enter the book title!")
            continue
        user_book_auther = input("Please enter the book auther: ")
        if user_book_auther == "":
            print("You need to enter the book auther!")
            continue
        user_book_isbn = input("Please enter the book ISBN: ")
        if user_book_isbn == "":
            print("You need to enter the book ISBN!")
            continue
        if not user_book_isbn.isdigit():
            print("The ISBN must be all digit!")
            continue
        add_book(library,user_book_title,user_book_auther, user_book_isbn)
        print("-"*15)
        user_choice = input("Please choose what you want to do: \n 1)add a new book to the library \n 2)remove a book from the library \n 3)Checkout a book \n 4)Return a book \n 5)Display all books \n To exit type 'exit': ")
    elif user_choice == "2":
        print()
        print("-"*15)
        user_book_isbn = input("Please enter the book ISBN: ")
        if user_book_isbn == "":
            print("You need to enter the book ISBN!")
            continue
        if not user_book_isbn.isdigit():
            print("The ISBN must be all digit!")
            continue
        remove_book(library, user_book_isbn)
        print("-"*15)
        user_choice = input("Please choose what you want to do: \n 1)add a new book to the library \n 2)remove a book from the library \n 3)Checkout a book \n 4)Return a book \n 5)Display all books \n To exit type 'exit': ")
    elif user_choice == "3":
        print()
        print("-"*15)
        user_book_isbn = input("Please enter the book ISBN: ")
        if user_book_isbn == "":
            print("You need to enter the book ISBN!")
            continue
        if not user_book_isbn.isdigit():
            print("The ISBN must be all digit!")
            continue
        check_out_book(library, user_book_isbn)
        print("-"*15)
        user_choice = input("Please choose what you want to do: \n 1)add a new book to the library \n 2)remove a book from the library \n 3)Checkout a book \n 4)Return a book \n 5)Display all books \n To exit type 'exit': ")
    elif user_choice == "4":
        print()
        print("-"*15)
        user_book_isbn = input("Please enter the book ISBN: ")
        if user_book_isbn == "":
            print("You need to enter the book ISBN!")
            continue
        if not user_book_isbn.isdigit():
            print("The ISBN must be all digit!")
            continue
        return_book(library, user_book_isbn)
        print("-"*15)
        user_choice = input("Please choose what you want to do: \n 1)add a new book to the library \n 2)remove a book from the library \n 3)Checkout a book \n 4)Return a book \n 5)Display all books \n To exit type 'exit': ")
    elif user_choice == "5":
        print()
        print("-"*15)
        display_books(library)
        print("-"*15)
        user_choice = input("Please choose what you want to do: \n 1)add a new book to the library \n 2)remove a book from the library \n 3)Checkout a book \n 4)Return a book \n 5)Display all books \n To exit type 'exit': ")
    else:
        print()
        print("-"*15)
        print("What you just typed isn't in the menu, Please try again")
        print("-"*15)
        user_choice = input("Please choose what you want to do: \n 1)add a new book to the library \n 2)remove a book from the library \n 3)Checkout a book \n 4)Return a book \n 5)Display all books \n To exit type 'exit': ")










