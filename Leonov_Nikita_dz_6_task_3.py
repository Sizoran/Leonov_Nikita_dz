import csv
from itertools import zip_longest
users = []
hobby = []
with open('users.csv', encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=",")
    for row in file_reader:
        test = ", ".join(row)
        test = (str(test).strip('\ufeff'))
        test = str(test).replace(', ', ' ')
        users.append(test)

with open('hobby.csv', encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=",")
    for row in file_reader:
        test = ", ".join(row)
        test = (str(test).strip('\ufeff'))
        test = str(test).replace(', ', ' ')
        hobby.append(test)

result_dict = dict(zip_longest(users, hobby))
print(result_dict)