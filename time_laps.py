# time装饰器
from functools import wraps
import time


def time_laps(func):
    """
    时间耗时装饰器
    :param func:
    :return:
    """

    @wraps(func)
    def wrap(*args, **kwargs):
        begin_time = time.perf_counter()
        result = func(*args, **kwargs)
        start_time = time.perf_counter()
        print('func:%r args:[%r, %r] took: %2.4f sec' % (func.__name__, args, kwargs, start_time - begin_time))
        return result

    return wrap
