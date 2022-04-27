class MyStaticMethod:
    """Emulate staticmethod"""

    def __init__(self, func):
        self.func = func

    def __get__(self, obj, objtype=None):
        return self.func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


class MyClassMethod:
    """Emulate classmethod"""

    def __init__(self, func):
        self.func = func

    def __get__(self, obj, cls=None):
        if cls is None:
            cls = type(obj)

        def new_func(*args):
            return self.func(cls, *args)

        return new_func


class MyClass:
    @staticmethod
    def func(x):
        return x * 3

    @MyStaticMethod
    def my_func(x):
        return x * 3

    @classmethod
    def func_2(cls):
        return cls()

    @MyClassMethod
    def my_func_2(cls):
        return cls()


class NewClass(MyClass):
    pass


if __name__ == '__main__':
    # test MyStaticMethod
    print(MyClass().func(3))
    print(MyClass().my_func(3))

    # test MyClassMethod
    print(type(MyClass.func_2()))
    print(type(NewClass.func_2()))
    print(type(MyClass.my_func_2()))
    print(type(NewClass.my_func_2()))
