name = 'Aditya'
age = 30


def display_data():
    name = 'Aditi'
    global age
    print(f'Name :{name} ,Age {age}')


if __name__ == '__main__':
    display_data()
