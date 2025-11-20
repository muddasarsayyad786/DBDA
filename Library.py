class DuplicateBookError(Exception):
    pass


def add_book(book_lst, book):
    for item in book_lst:
        if item[0] == book[0]:
            raise DuplicateBookError('Book with duplicate isbn exists')
    else:
        book_lst.append(book)


if __name__ == '__main__':
    book_list = [[123, 'Python1'], [345, 'Python2'], [456, 'Python3'], [678, 'Python4']]
    bk = [123, 'Python6']
    try:
        books_list = add_book(book_list, bk)
    except DuplicateBookError as e:
        print(e)
    else:
        print(books_list)
