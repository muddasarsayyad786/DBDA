def simple_function():
    print('This is a simple function')


simple_function()


def addition(num1: int, num2: int):
    return num1 + num2


result = addition(12, 13)
print(result)
result = addition(12.6, 13.9)
print(result)
result = addition((11, 12), (9, 8))
print(result)


def calculate_discount(product='table', price=5000):
    print(f'Discounted price for {product} is {price * 0.85}')


"""Positional arguments ve Keyword arguments
Positional args : both the type and position at which arg is given
is important
Keyword args : Only type not the position at which arg is given
is important
"""
calculate_discount('book', 900)
calculate_discount(price=900, product='book')
"""Default parameters : function can have default vales for parameters
However when a parameter is given a default value all the following params
must also have a default value"""
calculate_discount()
calculate_discount('chair')
calculate_discount(price=1000)

"""
Variable arguments : when function receives var args, it can take any number
of arguments. or can also take list/tuple/dict value as an input
"""


def add(*nums):
    total = 0
    for num in nums:
        total += num
    print(total)


numbers = [12, 23, 3, 4, 5, 6, 78]
student = {
    'name': 'prr',
    'marks': [90, 89, 78, 89]
}

add(12, 13, 5, 6, 7, 8, 9, 10, 11)
add(*numbers)
add(*student['marks'])

"""
Variable Keyword arguments :
when function receives var keyword args, it can take any number
of keyword arguments. or can also take dict as an input
"""


def calculate_average(**kwargs):
    values = kwargs['marks']
    total = 0
    for val in values:
        total += val
    print(f'Average marks for {kwargs["name"]} = {total / len(values)}')


calculate_average(name='adf', marks=[98, 78, 90, 87])
calculate_average(**student)
