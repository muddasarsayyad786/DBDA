for i in range(10):
    if i == 5:
        break
    print(i)

print('----------------------')
for i in range(10):
    if i == 5:
        continue
    print(i)

print('----------------------')
for i in range(1, 11, 2):
    print(i)

print('----------------------')
st = "this is a string"
for ch in st:
    print(ch)

print('----------------------')
isprime = True
num = int(input('Enter a number '))
for i in range(2, num):
    if num % i == 0:
        isprime = False
        break
if isprime:
    print('Number is prime')
else:
    print('Number is not prime')

print('-------------------')
""" else -for
else will execute if loop terminates naturally
"""
num = int(input('Enter a number '))
for i in range(2, num):
    if num % i == 0:
        print('Number is not prime')
        break
else:
    print('Number is prime')
