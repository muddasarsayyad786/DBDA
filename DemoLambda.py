def increment(n):
    return n + 1


incre = increment
print(incre(20))

incre = lambda n: n + 1
print(incre(30))

l0 = lambda: 100
print(l0())

l1 = lambda n1, n2, n3=6: n1 + n2 + n3
print(l1(1, 2, 3))
print(l1(n1=1, n2=2, n3=3))
print((l1(5, 7)))

my_list = [1, 2, 3, 4]
l2 = lambda *args: sum(args)
print(l2(1, 2, 3, 4, 5, 5, 6))
print(l2(*my_list))

data = {'one': 1,
        'two': 2,
        'three': 3}
l3 = lambda **kwargs: sum(kwargs.values())
print(l3(one=1, two=2, three=3))
print(l3(**data))
