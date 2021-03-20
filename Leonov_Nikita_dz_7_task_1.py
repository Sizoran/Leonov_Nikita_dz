import os

dir_name = 'my_project'
under_dir_names = ['settings', 'mainapp', 'adminapp', 'authapp']
name_count = 0
while name_count < len(under_dir_names):
    mkdir_name = os.path.join(dir_name, under_dir_names[name_count])  # В методичке хорошо описана данная ситуация
    if not os.path.exists(mkdir_name):
        os.makedirs(mkdir_name)
    name_count += 1