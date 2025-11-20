def get_data():
    n = 1
    while True:
        yield n
        n += 1


series = get_data()
print(next(series))
print(next(series))
print(next(series))
print(next(series))


def gen_fib(end):
    i = 0
    a, b = 0, 1
    while i < end:
        yield b
        a, b = b, b + a
        i += 1


fib_series = gen_fib(10)
print(next(fib_series))
print(next(fib_series))
print(next(fib_series))
print(next(fib_series))
print(next(fib_series))
print(next(fib_series))