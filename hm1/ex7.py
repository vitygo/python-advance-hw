def multiply(x, y):
    return x * y

from functools import partial

multiply_curried = partial(multiply)


multiply_by_5 = partial(multiply, 5)
multiply_by_5_and_10 = partial(multiply, 5, 10)


print(multiply_by_5(3)) 
print(multiply_by_5_and_10()) 