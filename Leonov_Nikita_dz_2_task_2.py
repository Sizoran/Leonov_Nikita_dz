weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for item_id, item in enumerate(weather):
    if (item.isdigit() or (item.isalnum() is False and item != '"')) and weather[item_id - 1] != '"':
        if item.isalnum() is False and len(item[1:]) < 2:
            weather[item_id] = f'{item[0]}0{item[1:]}'
        elif len(item) < 2:
            weather[item_id] = f'0{item}'
        weather.insert(item_id, '"')
        weather.insert(item_id + 2, '"')
print(weather)  # вывожу для проверки выполнения задания по добавлению ковычек
print(f'{weather[0]} {weather[1]}{int(weather[2]):02d}{weather[3]} {weather[4]} {weather[5]}'
      f'{int(weather[6]):02d}{weather[7]} {weather[8]} {weather[9]} {weather[10]} {weather[11]} '
      f'{weather[12]}{weather[13]}{weather[14]} {weather[15]}')