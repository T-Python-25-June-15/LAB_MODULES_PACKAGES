#lab modules and packages wasan alqahtani
from library import librarian

try:
    library = {}
    while True:
        print("Welcome to library program")
        print("-"*20)
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Check Out Book")
        print("4. return Availability")
        print("5. Display All Book")
        print("6. Exit")
        print("-"*20)
        print("\n")
        option = input("please choose from the menue above:")
        
        match option:
            case "1":
                print("Add Book")
                print("-"*20)
                title = input("please enter title name: ")
                author = input("please enter author name: ")
                Isbn= input("please enter isbn number: ")
                librarian.add_book(library,title,author,Isbn)
           
            case "2":
                print("Remove Book")
                print("-"*20)
                Isbn= input("please enter isbn number: ")
                librarian.remove_book(library,Isbn)
            case "3":
                print("Check out")
                print("-"*20)
                Isbn= input("please enter isbn number: ")
                librarian.check_out_book(library,Isbn)
            case "4":
                print(" Return Book")
                print("-"*20)
                Isbn= input("please enter isbn number: ")
                librarian.return_book(library,Isbn)
            case "5":
                print(" Display All Book")
                print("-"*20)
                librarian.display_books(library)
            case "6":
                break
            case  _:
                print("wrong number try again")
except Exception as e:
    print(e.__class__, e)