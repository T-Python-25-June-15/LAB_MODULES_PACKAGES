from library.librarian import *
library: dict = {}

# Add books and then display it
add_book(library, "The Catcher in the Rye" ,"J.D. Salinger" , "9780316769174")
add_book(library, "To Kill a Mockingbird" ,"Harper Lee" , "9780446310789")
add_book(library, "1984" ,"George Orwell" , "9780451524935")
display_books(library)
print()

# Check out a book and then display all books
check_out_book(library, "9780316769174")
display_books(library)
print()

# Return a book and then display all books
return_book(library, "9780316769174")
display_books(library)
print()

# Remove a book and then display all books
remove_book(library, "9780316769174")
display_books(library)