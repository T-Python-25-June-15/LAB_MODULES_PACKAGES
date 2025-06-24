from library import librarian

my_library = {}
librarian.add_book(my_library, "The Catcher in the Rye", "J.D. Salinger", "9780316769174")
librarian.add_book(my_library, "To Kill a Mockingbird", "Harper Lee", "9780446310789")
librarian.add_book(my_library, "1984", "George Orwell", "9780451524935")

print("\nAll Books:")
librarian.display_books(my_library)

librarian.check_out_book(my_library, "9780316769174")

print("\nAfter checking out one book:")
librarian.display_books(my_library)

librarian.return_book(my_library, "9780316769174")

print("\nAfter returning the book:")
librarian.display_books(my_library)

librarian.remove_book(my_library, "9780451524935")

print("\nAfter removing a book:")
librarian.display_books(my_library)
