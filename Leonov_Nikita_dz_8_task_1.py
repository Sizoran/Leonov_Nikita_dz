import re

user_emails = ['basil2021@geekbrains.ru', 'basil-2@geekbrainsru', 'olly@mail.com']
valid_date = re.compile(r'\w+[/@]\w+[/.]\w+')


def email_parse(args):
    for i in args:
        try:
            assert valid_date.match(i)
            print({
                'username': re.compile(r'(\w+)\@').findall(i)[0],
                'domain': re.compile(r'[@](\w+)').findall(i)[0]
            })
        except AssertionError:
            print('ValueError: wrong email: ', i)

email_parse(user_emails)