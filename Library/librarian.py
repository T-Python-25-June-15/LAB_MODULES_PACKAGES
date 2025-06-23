



def add_book(library:dict, title:str, author:str, isbn:str):

    book = {
        'title': title,
        'author': author,
        'isbn': isbn,
        'available': True
    }
   
    if isbn not in library.keys():
        library[isbn] = book
    else:
        print('no')

    



# library = {
#     '1221': {'title': 'Oppenheimer', 'author': 'Abood', 'isbn': '1221', 'available': True},
#     '125': {'title': 'Some Book', 'author': 'Ajmad', 'isbn': '125', 'available': True}
# }

# add_book(library, "asda", "mohammed", '1245')
# print(library)

def remove_book(library, isbn):
    pass




def check_out_book(library, isbn):
    pass




def return_book(library, isbn):
    pass



def display_books(library):
    pass


