from library import librarian
def main():
    books_library={}
    librarian.add_book(books_library,"The Catcher in the Rye" ,"J.D. Salinger","1234")
    librarian.add_book(books_library,"To Kill a Mockingbird " ,"Harper Lee","12345")
    librarian.add_book(books_library,"1984 " ,"George Orwell","123456")

    librarian.display_books(books_library)
    librarian.check_out_book(books_library,"123456")
    librarian.check_out_book(books_library,"1234")
    librarian.return_book(books_library,"12345")
    librarian.remove_book(books_library,"1234")
    librarian.display_books(books_library)
main()
