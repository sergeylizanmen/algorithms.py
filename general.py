import timeit

from typing import Callable, Any
import functools


def timer(func: Callable) -> Callable:
    """ Декоратор-таймер """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = timeit.default_timer()
        res = func(*args, **kwargs)
        run_time = round(timeit.default_timer() - start_time, 8)
        print('\nВремя выполнения {}: {:.8f}'.format(func.__name__, run_time))
        return res

    return wrapper
