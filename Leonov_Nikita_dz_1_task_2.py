my_list = []
my_sum_1 = 0
my_sum_2 = 0
for i in range(1, 1001, 2):
    my_list.append(i ** 3)
for el in my_list:
    random_sum = 0
    random_list = list(str(el))
    for i in random_list:
        random_sum += int(i)
    if random_sum % 7 == 0:
        my_sum_1 += el

for el in my_list:
    random_sum = 0
    random_list = list(str(el + 17))  # Добавляю к каждому элементу 17
    for i in random_list:
        random_sum += int(i)
    if random_sum % 7 == 0:
        my_sum_2 += el
print(my_sum_1)
print(my_sum_2)