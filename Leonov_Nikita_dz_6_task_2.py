with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    nginx_logs = f.read()
nginx_logs = nginx_logs.splitlines()
spam_find_list = []
for el in nginx_logs:
    remote_addr = el.split('- -')[0]
    spam_find_list.append(remote_addr)


for index, val in enumerate(spam_find_list):
    if val != spam_find_list[index - 1]:   # Вот тут я пытался сделать что бы не печатало повторение, но не смог.
        if spam_find_list.count(val) > 2000:  # Вот тут можно менять кол-во обращений и он выдаст все
            # которые превышают указанный порог, только надо убрать break
            print(f'SPAM: {val} кол-во запросов {spam_find_list.count(val)}')
            break