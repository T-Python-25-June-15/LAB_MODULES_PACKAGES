from library import librarian

library = {}

while True:
    print("\n--- Library Menu ---")
    print("1. Add a book")
    print("2. Check out a book")
    print("3. Return a book")
    print("4. Display all books")
    print("5. Remove a book") 
    print("6. Exit")          

    choice = input("Enter your choice (1-6): ") 

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        isbn = input("Enter ISBN: ")
        result = librarian.add_book(library, title, author, isbn)
        print(result)

    elif choice == "2":
        isbn = input("Enter ISBN to check out: ")
        result = librarian.check_out_book(library, isbn)
        print(result)

    elif choice == "3":
        isbn = input("Enter ISBN to return: ")
        result = librarian.return_book(library, isbn)
        print(result)

    elif choice == "4":
        librarian.display_books(library)

    elif choice == "5":
        isbn = input("Enter ISBN to remove: ")
        result = librarian.remove_book(library, isbn)
        print(result)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.") 