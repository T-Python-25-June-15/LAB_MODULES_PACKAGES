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