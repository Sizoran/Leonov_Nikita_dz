my_list = []

for i in range(1, 1000, 2):
    my_list.append(i ** 3)
for el in my_list:
    random_sum = 0
    random_list = list(str(el))
    for i in random_list:
        random_sum += int(i)
    if random_sum % 7 == 0:
        print(el)

for el in my_list:
    random_sum = 0
    random_list = list(str(el + 17))  # Добавляю к каждому элементу 17
    for i in random_list:
        random_sum += int(i)
    if random_sum % 7 == 0:
        print(el)
