user_num = int(input('Введите число до которого будет производиться вычисления: '))
user_num = (print(el) for el in range(1, user_num + 1, 2))


print(type(user_num))
next(user_num)
next(user_num)
next(user_num)