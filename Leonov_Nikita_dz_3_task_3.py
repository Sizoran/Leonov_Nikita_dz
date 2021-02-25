def thesaurus(*args):
    res_tuple = {}
    for i in args:
        if res_tuple.get(i[0]) is None:
            res_tuple[i[0]] = []
            res_tuple[i[0]].append(i)
        else:
            res_tuple[i[0]].append(i)

    print(res_tuple)


thesaurus("Иван", "Мария", "Петр", "Илья", "Томара", "Тоня", "Андрей")