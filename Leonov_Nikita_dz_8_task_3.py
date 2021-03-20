def p_wrapper(func):

    def tag_wrapper(args):
        markup = func(args)
        print(f'{func.__name__}({args}: {type(markup)})')
        return markup

    return tag_wrapper


@p_wrapper
def calc_cube(x):
    return x ** 3


calc_cube(3)


def p_wrapper(func):    # Это если аргументов много
    def tag_wrapper(*args):
        for arg in args:
            print(f'{arg}: {type(arg)}', end=', ')
        return func(args[0])
    return tag_wrapper


@p_wrapper
def calc_cube(x):
    return x ** 3


calc_cube(3, 5.5, 'Строка', ['Список'], ('кортеж',), {'Словарь': 1})