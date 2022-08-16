import functools


def uppercase_decorator(function):
    @functools.wraps(function)
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

