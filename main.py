# from library.librarian import display_books,add_book,remove_book,return_book
import library.librarian as libr


library = {}

def mainmenu():
    while True:
        try:
            print("""
                1- Add Book
                2- Remove Book
                3- Check Out Book
                4- Return Book
                5- Display Books
                """)
            option = int(input("Enter your option: "))
            if option == 1:
                title = input("Enter the title: ")
                author = input("Enter the Author: ")
                isbn = int(input("Enter the ISBN: "))
                libr.add_book(library,title,author,isbn)

            elif option == 2:
                isbn = int(input("Enter the ISBN: "))
                libr.remove_book(library, isbn)

            elif option == 3:
                isbn = int(input("Enter the ISBN: "))
                libr.check_out_book(library, isbn)

            elif option == 4:
                isbn = int(input("Enter the ISBN: "))
                libr.check_out_book(library, isbn)

            elif option == 5:
                isbn = int(input("Enter the ISBN: "))
                libr.display_books(library)

            else:
                print("Wrong input")

                # library, title, author, isbn
        except Exception as ex:
            print(f"There was an error :{ex}")

mainmenu()