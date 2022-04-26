from functools import wraps


def decorate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@decorate
def multiply(a=3, b=2):
    return a*b


if __name__ == '__main__':
    print(multiply)
