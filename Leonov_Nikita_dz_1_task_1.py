duration = int(input('Введите кол-во секунд для конвертирования: '))

sec = duration % 60
minutes = (duration // 60) % 60
hours = (duration // 3600) % 24
days = duration // (60 * 60 * 24)

print(f' результат: {days} дн {hours} час {minutes} мин {sec} сек')