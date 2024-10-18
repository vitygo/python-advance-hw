import time



def how_long(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func()
        t2 = time.time() - t1
        print(f"it took {t2} seconds to executee")
    
    return wrapper


@how_long
def first_func():
    for num in range(10000000):
        if num ==5000000:
            print('hello world')
@how_long
def second_func():
    for num in range(10000000):
        if num ==6000000:
            print('yes world')

first_func()
second_func()