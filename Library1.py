class DuplicateBookError(Exception):
    pass


def create_list(book):
    book_list = [[123, 'Python1'], [345, 'Python2'], [456, 'Python3'], [678, 'Python4']]
    book_list.append(book)
    return book_list


def add_book(book_lst, book):
    for item in book_lst:
        if item[0] == book[0]:
            print('in if')
            raise DuplicateBookError('Book with duplicate isbn exists')
    else:
        print('in else')
        create_list(book)
        return book_lst


if __name__ == '__main__':

    bk = [123, 'Python6']
    try:
        books_list = add_book(book_list, bk)
    except DuplicateBookError as e:
        print(e)
    else:
        print(books_list)
