duration = int(input('Введите кол-во секунд для конвертирования: '))

if duration <= 60:
    print(f' результат: {duration} сек')
elif duration <= 3600:
    print(f' результат: {duration // 60} мин {duration % 60} сек')
elif duration <= 86400:
    print(f' результат: {(duration // 3600) % 24} час {(duration // 60) % 60} мин {duration % 60} сек')
elif duration <= 2678400:
    print(f' результат: {(duration // 86400) % 31} дн {(duration // 3600) % 24} час {(duration // 60) % 60} мин '
          f'{duration % 60} сек')
else:
    print('Введённое число больше 31 дня и мощности процессора не хварает для расчёта... ')