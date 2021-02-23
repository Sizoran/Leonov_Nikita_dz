price_in_rub = [57.8, 46.51, 97, 198, 15, 90, 11, 67.98, 1.10, 85.1, 2, 67, 6233, 133, 9.76]
print('id =', id(price_in_rub))
for el in price_in_rub:
    print(f'{int(el * 100) // 100} руб {int(el * 100) % 100} коп')  # Задание А
print('id =', id(price_in_rub))
for el in sorted(price_in_rub):
    print(f'{int(el * 100) // 100} руб {int(el * 100) % 100} коп')  # Задание В
print('id =', id(price_in_rub))
new_price_in_rub = sorted(price_in_rub, reverse=True)  # Задание С
print(new_price_in_rub)

# Далее выведу список топ-5 товаров по цене используюя счётчик (ТОП) по заданию D
top_5_price = new_price_in_rub[0:5]
item_count = 5
for el in reversed(top_5_price):
    print(f'Товар топ {item_count} - {int(el * 100) // 100} руб {int(el * 100) % 100} коп')
    item_count -= 1