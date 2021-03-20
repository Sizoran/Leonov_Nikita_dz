import os
import shutil

root_dir = r'C:\Users\Sizoran\Desktop\Gig Study\Основы языка Python\Stady_v2.0\hw_7\my_project'
for root, dirs, files in os.walk(root_dir):
    print(root, dirs)

start_root_1 = r'C:\Users\Sizoran\Desktop\Gig Study\Основы языка Python\Stady_v2.0\hw_7\my_project\authapp\templates'
start_root_2 = \
    r'C:\Users\Sizoran\Desktop\Gig Study\Основы языка Python\Stady_v2.0\hw_7\my_project\mainapp\templates\mainapp'
try:
    shutil.move(start_root_1, root_dir)
except:
    pass

root_dir = r'C:\Users\Sizoran\Desktop\Gig Study\Основы языка Python\Stady_v2.0\hw_7\my_project\templates'
try:
    shutil.move(start_root_2, root_dir)
except:
    pass