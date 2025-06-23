import library.librarian as librarian

library = {}

#Adding Book
librarian.add_book(library, "The Catcher in the Rye", "J.D. Salinger", "3252523523523")
librarian.add_book(library, "To Kill a Mockingbird", "Harper Lee", "9780446310789")
librarian.add_book(library, "1984", "George Orwell", "9780451524935")
librarian.add_book(library, "The Little Prince", "Antoine de Saint-Exupéry", "9780451524935") #duplicate

#Display Books
librarian.display_books(library)

#CheckOut Book
librarian.check_out_book(library, "3252523523523")
librarian.check_out_book(library, "0000000000000")
librarian.check_out_book(library, "3252523523523")

#Display Books
librarian.display_books(library)

#Returning Book
librarian.return_book(library, "3252523523523")
librarian.return_book(library, "9999999999999")

#Display Books
librarian.display_books(library)

#Removing Book
librarian.remove_book(library, "9780451524935")
librarian.remove_book(library, "1111111111111")

#Display Books
librarian.display_books(library)