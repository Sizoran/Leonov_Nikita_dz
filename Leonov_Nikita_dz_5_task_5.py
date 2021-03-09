src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_src = [el for el in src if src.count(el) == 1]  # Решение "в лоб"
print(unique_src)

unique_src_2 = set(src)  # Оптимизация как по методичке
tmp = set()
for el in src:
    if el not in tmp:
        unique_src_2.add(el)
    else:
        unique_src_2.discard(el)
    tmp.add(el)
unique_src_2_ord = [el for el in src if el in unique_src_2]
print(unique_src_2_ord)