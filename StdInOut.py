name = input('Enter your name : ')
age = int(input('Enter your age : '))

print('You have entered name : ', name, ' and age :', age)
print('You have entered name: {} and age: {}'.format(name, age))
print(f'You have entered name: {name} and age: {age}')

val = 4e5
print(val)

val = 4e6
print(val)
print(f'{val/1e6:.2f}M')

val = 234
print(f'{val/100:.1f}%')

