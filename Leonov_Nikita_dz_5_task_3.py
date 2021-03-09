from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Никита', 'Basil']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А']


def comp_list(list_1, list_2):
    yield zip_longest(list_1, list_2, fillvalue=None)


comp_result = comp_list(tutors, classes)
print(type(comp_result))
print(*next(comp_result))