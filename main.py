from library import librarian
my_library = {}

librarian.add_book(my_library, 'The Hitchhikers Guide to the Galaxy', 'Douglas Adams', '111')
librarian.add_book(my_library, 'Pride and Prejudice', 'Jane Austen', '221')
librarian.add_book(my_library, 'The Great Gatsby', 'F. Scott Fitzgerald', '331')



librarian.remove_book(my_library, '221')
print("="*50)
librarian.check_out_book(my_library, '331')
print("="*50)
librarian.display_books(my_library)


