import functools
#Рекурсия

@functools.lru_cache()
def fib(n):
    
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

#Рекурсия + мемоизация

def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]
        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]

    return _fib_dict(n)

#Цикл

def fib_loop(n):
    if n < 2:
        return n

    first = 0
    second = 1

    for _ in range(2, n + 1):
        first, second = second, first + second
    return second


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

#test_fib(fib)
#test_fib(fib_dict)
test_fib(fib_loop)