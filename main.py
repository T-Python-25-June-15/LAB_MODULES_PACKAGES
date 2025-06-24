from library import librarian

library = {}

print(library)


librarian.add_book(library, "Clean Code", "Robert C. Martin", "9780132350884")

librarian.add_book(library, "The Hobbit", "J.R.R. Tolkien", "9780261102217")
librarian.add_book(library, "The Hobbit", "J.R.R. Tolkien", "9780261102217")
librarian.add_book(library, "Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "9780590353427")
librarian.display_books(library)

print("-"*30)
librarian.remove_book(library, "9780261102217")
librarian.check_out_book(library, "9780132350884")
print("-"*30)
librarian.display_books(library)
librarian.return_book(library, "9780132350884")
print("-"*30)
librarian.display_books(library)












