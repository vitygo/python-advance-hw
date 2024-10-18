def fibonacci_no_cache(n):
    if n <= 1:
        return n
    return fibonacci_no_cache(n - 1) + fibonacci_no_cache(n - 2)

fibonaci = [fibonacci_no_cache(x) for x in range(10)]

print(fibonaci)

#----------------------------------

from functools import lru_cache

@lru_cache(maxsize=10)
def fibonacci_lru_cache_10(n):
    if n <= 1:
        return n
    return fibonacci_lru_cache_10(n - 1) + fibonacci_lru_cache_10(n - 2)

fibonaci = [fibonacci_lru_cache_10(x) for x in range(10)]

print(fibonaci)