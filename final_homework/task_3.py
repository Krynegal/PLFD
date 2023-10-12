def cache_decorator(function):
    cache = {}

    def wrapper(*args, **kwargs):
        if args in cache:
            return cache[args]
        else:
            res = function(*args, **kwargs)
            cache[args] = res
            return res

    return wrapper


@cache_decorator
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(100))
