def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

func = fib(10)
print(next(func))
print(next(func))
print(next(func))
print(next(func))