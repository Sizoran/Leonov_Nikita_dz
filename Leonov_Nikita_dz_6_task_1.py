with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    nginx_logs = f.read()
nginx_logs = nginx_logs.splitlines()
for el in nginx_logs:
    remote_addr = el.split('- -')[0]
    request_type = el.split('"')[1].split()[0]
    requested_resource =el.split('"')[1].split()[1]
    result_tuple = (remote_addr, request_type, requested_resource)
    print(result_tuple)