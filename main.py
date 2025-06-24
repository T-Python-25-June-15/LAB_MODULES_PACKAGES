from library import librarian

library = {}

while True:
    print("-"*26)
    print("Welcome to library program")
    print("-"*26)
    print()
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Check Out Book")
    print("4. return Availability")
    print("5. Display All Book")
    print("6. Exit")
    print()
    print()
    option = int(input("Choose a number: "))
    print("-" * 18)

    match option:
        case 1:
            print("Add Book")
            print()
            title = input("Enter title name: ")
            author = input("Enter author name: ")
            isbn= input("Enter ISBN number: ")
            librarian.add_book(library,title,author,isbn)
            print()
            print()

        case 2:
            print("Remove Book")
            print()
            Isbn= input("Enter ISBN number: ")
            librarian.remove_book(library,Isbn)
            print()
            print()
        case 3:
            print("Check out")
            print()
            Isbn= input("Enter ISBN number: ")
            librarian.check_out_book(library,Isbn)
            print()
            print()
        case 4:
            print(" Return Book")
            print()
            Isbn= input("Enter ISBN number: ")
            librarian.return_book(library,Isbn)
            print()
            print()
        case 5:
            print(" Display All Book")
            print()
            librarian.display_books(library)
            print()
            print()
        case 6:
            print("Thanks, we hope to see you again.")
            break
        case  _:
            print("Invalid inputs, only numbers.")
    