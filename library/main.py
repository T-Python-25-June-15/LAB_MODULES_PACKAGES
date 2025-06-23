import librarian

library={}

librarian.add_book(library,"The Catcher in the Rye" ,"by J.D. Salinger "," 9780316769174")
librarian.add_book(library, "To Kill a Mockingbird", "Harper Lee", "9780446310789")
librarian.add_book(library, "1984", "George Orwell", "9780451524935")

print("ccurrent")

librarian.check_out_book(library,"9780316769174")
print("after checking")
librarian.display_book(library)
librarian.return_book(library,"9780316769174")
print("after returning")
librarian.display_book(library)