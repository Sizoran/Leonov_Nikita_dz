def thesaurus_adv(*args):
    res_tuple = {}
    for i in args:
        el = str(i).split()
        if res_tuple.get(el[1][0]) is None:
            res_tuple[el[1][0]] = []
            res_tuple[el[1][0]].append(i)
        else:
            res_tuple[el[1][0]].append(i)

    print(res_tuple)


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Донни Трамп",
              "Билл Гейтц")

# К сожалению я не смог додуматься как сделать дальше :(