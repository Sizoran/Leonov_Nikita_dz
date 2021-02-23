list_stat = {'инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита'}
for el in list_stat:
    new_list = el.split(' ')
    name = new_list[-1]
    print('Привет, ', name.capitalize())
# Медото без создания списка:
for el in list_stat:
    print('Привет, ', (el.split(" ")[-1]).capitalize())