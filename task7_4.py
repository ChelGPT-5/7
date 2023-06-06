import time

def time_operation(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Функция выполнялась {end-start:.2f} секунд')
        return result
    return wrapper

@time_operation
def my_function(a, b):
    time.sleep(3)
    return a + b


result = my_function(1, 5)