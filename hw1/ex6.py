def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def even_filter_decorator(func):
    def wrapper(*args, **kwargs):
        for num in func(*args, **kwargs):
            if num % 2 == 0:
                yield num
    return wrapper

@even_filter_decorator
def even_fibonacci_generator():
    return fibonacci_generator()

gen = even_fibonacci_generator()

for _ in range(10):
    print(next(gen))