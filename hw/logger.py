import timeit
import functools

def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timer = timeit.Timer(lambda: func(*args, **kwargs))
        print(f"Выполнение метода {func.__name__} началось.")
        result = func(*args, **kwargs)
        execution_time = timer.timeit(number=1)
        print(f"Выполнение метода {func.__name__} завершилось. Время выполнения: {execution_time:.8f} секунд.")
        return result
    return wrapper
