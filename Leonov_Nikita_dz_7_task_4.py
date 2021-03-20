import os

import django

file_100 = 0
file_1000 = 0
file_10000 = 0
file_100000 = 0

root_dir = django.__path__[0]
for root, dirs, files in os.walk(root_dir):
    for i in files:
        i = os.path.join(root, i)
        if os.stat(i).st_size < 100:
            file_100 += 1
        elif os.stat(i).st_size < 1000:
            file_1000 += 1
        elif os.stat(i).st_size < 10000:
            file_10000 += 1
        elif os.stat(i).st_size < 100000:
            file_100000 += 1

final_dict = {
    100: file_100,
    1000: file_1000,
    10000: file_10000,
    100000: file_100000
}

print(final_dict)