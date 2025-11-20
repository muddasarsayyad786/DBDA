from builtins import print

i = 10
print(type(i))
print(id(i))
print(i)

j = 10
print(id(j))

print(i == j)  # both var have same value
print(i is j)  # Both refer to the same object

k = 23.6
print(type(k))
print(k)

c = complex(i, j)
print(c)
print(type(c))

flag = True
print(type(flag))
print(flag)

s = "this is a string"
print(type(s))
print(s)

m = [10, 20]
n = [10, 20]
print(type(m))
print(m == n)
print(m is n)

p = m
print(m is p)
m.append(30)
print(m)
print(n)
print(p)

t = (1, 2, 3)
print(type(t))

st = {1, 2, 3}
print(type(st))

d = {1: 'one', 2: 'two'}
print(type(d))


i = int(k)
print(i)

k = float(i)
print(k)

st = '23.4'
k = float(st)
print(k)
