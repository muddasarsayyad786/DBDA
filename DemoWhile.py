i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

print('---------------')
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)

print('---------------')
num = int(input('Enter a number '))
i = 2
while i < num:
    if num % i == 0:
        print('Number is not prime')
        break
    i += 1
else:
    print('Number is prime')

