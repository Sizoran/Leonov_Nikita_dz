def num_generator(user_input_num):
    for el in range(1, user_input_num + 1, 2):
        yield print(el)

user_num = num_generator(int(input('Введите число до которого будет производиться вычисления: ')))

print(type(user_num))
next(user_num)
next(user_num)
next(user_num)