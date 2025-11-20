# age = int(input('Enter your age '))
# gender = input('Enter gender M/F ')
# if age > 18:
#     print('You are an adult')
# else:
#     print('You are a child')
#
# if age > 18:
#     if gender == 'M':
#         print('You are a man')
#     else:
#         print('You are a lady')
# else:
#     print('You are child')
#
# if age > 18 and gender == 'M':
#     print('You are a man')
# elif age > 18 and gender == 'F':
#     print('You are a lady')
# else:
#     print('You are child')

"""multiple ifs : each if is evaluated separately
else will execute if any of the ifs fail
"""
marks = int(input('Enter marks'))
if 80 <= marks < 100:
    print('A')
if 60 <= marks < 80:
    print('B')
if 40 <= marks < 60:
    print('c')
else:
    print('D')

"""
if-elif : else will execute only if all the ifs fail
"""
marks = int(input('Enter marks'))
if 80 <= marks < 100:
    print('A')
elif 60 <= marks < 80:
    print('B')
elif 40 <= marks < 60:
    print('c')
else:
    print('D')
