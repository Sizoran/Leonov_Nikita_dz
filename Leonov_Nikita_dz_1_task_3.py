random_int = int(input('Введите число от 1 до 20: '))

if random_int == 1:
    print(random_int, 'процент')
elif random_int == 2 or random_int == 3 or random_int == 4:
    print(random_int, 'процента')
elif random_int >= 5:
    print(random_int, 'процентов')
elif random_int > 20:
    print('Не верно введено число')
