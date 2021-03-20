def val_checker(callback):
    def the_real_decorator(function):
        def wrapper(*args):
            if callback(*args):
                return function(*args)
            else:
                print('ValueError: wrong val: ', args[0])

        return wrapper

    return the_real_decorator


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
a = calc_cube(-5)
print(a)