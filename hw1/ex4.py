import time
from functools import lru_cache


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} executed in {execution_time:.5f} seconds")
        return result
    return wrapper


def fibonacci_no_cache(n):
    if n <= 1:
        return n
    return fibonacci_no_cache(n - 1) + fibonacci_no_cache(n - 2)


fib_cache = {}

def fibonacci_with_cache(n):
    if n in fib_cache:
        return fib_cache[n]
    if n <= 1:
        result = n
    else:
        result = fibonacci_with_cache(n - 1) + fibonacci_with_cache(n - 2)
    fib_cache[n] = result
    return result


@lru_cache(maxsize=10)
def fibonacci_lru_cache_10(n):
    if n <= 1:
        return n
    return fibonacci_lru_cache_10(n - 1) + fibonacci_lru_cache_10(n - 2)


@time_decorator
def test_fibonacci_no_cache():
    for i in range(25):
        fibonacci_no_cache(i)

@time_decorator
def test_fibonacci_with_cache():
    for i in range(25):
        fibonacci_with_cache(i)

@time_decorator
def test_fibonacci_lru_cache_10():
    for i in range(25):
        fibonacci_lru_cache_10(i)

# Запуск тестів
test_fibonacci_no_cache()
test_fibonacci_with_cache()
test_fibonacci_lru_cache_10()
