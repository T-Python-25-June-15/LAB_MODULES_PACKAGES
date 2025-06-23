from library.librarian import *

CYAN = "\033[36m" # color for terminal
RESET = "\033[0m" # color for terminal

lib = {}

def printHomePage():
    print(CYAN + "1. Diplay all books\n2. Add book\n3. Remove book\n4. Check out\n5. Return book\n6. Exit" + RESET)
    
def main():
    global lib
    lib = add_book(lib, "The Catcher in the Rye", "J.D. Salinger", "9780316769174")
    lib = add_book(lib, "To Kill a Mockingbird", "Harper Lee", "9780446310789")
    lib = add_book(lib, "1984", "George Orwell", "9780451524935")
    
    while True:
        printHomePage()
        try:
            user_input = int(input("Enter your choice: "))
            match user_input:
                case 1: display_books(lib)
                case 2: lib = add_book(lib, input("Title: "), input("Auther: "), input("ISBN: "))
                case 3: lib = remove_book(lib, input("ISBN: "))
                case 4: lib = check_out_book(lib, input("ISBN: "))
                case 5: lib = return_book(lib, input("ISBN: "))
                case 6: break
                
        except Exception as e:
            print("Invalied input, please try again.")
    
main()