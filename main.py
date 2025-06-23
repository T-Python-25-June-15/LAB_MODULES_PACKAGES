from library import librarian

library = []

librarian.add_book(library, "Test book", "MESHARI", "110")
librarian.add_book(library, "The Catcher in the Rye by J.D", "Salinger", "9780316769174")
librarian.add_book(library, "To Kill a Mockingbird", "Harper Lee", "9780446310789")

librarian.display_books(library)


librarian.check_out_book(library, "110")
librarian.display_books(library)



librarian.return_book(library, "110")
librarian.display_books(library)



librarian.remove_book(library, "110")
librarian.display_books(library)