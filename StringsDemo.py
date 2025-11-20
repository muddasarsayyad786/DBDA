s = "Python is a dynamic language"

is_present = 'Python' in s
print(is_present)

not_present = 'Java' not in s
print(not_present)

print('-----------Indexing & Slicing-----------')
print(s[8])
print(s[-8])
print(s[3:10])
print(s[-10:-3])
print(s[-3:-10])
# print(s[40]) # IndexError: string index out of range
print(s[2:14:2])
print(s[3:10:-2])
print(s[12:2:-1])
print(s[::-1])
print(s[:10])
print(s[10:])
print(s[:10] + s[10:])

print('-------Char classification------------')
s1 = 'helloA'
print(s1.isalpha())
s1 = '1234'
print(s1.isdecimal())
s1 = '12\u00B2'
print(s1.isdigit())
s1 = '12\u00B2\u2168'
print(s1.isnumeric())
s1 = 'abc12\u00B2\u2168'
print(s1.isalnum())
print(s1.isprintable())
print(s1.isidentifier())
print(s1.isspace())

print('--------- case conversion---------')
s2 = 'Welcome to Python'
print(s2.lower())
print(s2.upper())
print(s2.title())
print(s2.capitalize())
print(s2.swapcase())

print('--------- other methods ---------')
s3 = '   sit bit fit chit sit   '
s3 = s3.strip()
words = s3.split(' ')
print(words)
print(s3.count('sit'))
s4 = ','.join(words)
print(s4)
partition = s4.partition('fit')
print(partition)
s4 = s4.replace(',', '-')
print(s4)
