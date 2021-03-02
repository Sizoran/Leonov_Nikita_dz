from datetime import datetime


def currency_rates(char_code):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    ask_content = str(response.content)
    ask_content = list(ask_content.split('ID'))
    ask_date = ask_content[0].split()  # Вот тут нахожу дату запроса
    ask_date = ask_date[3][6:-1]
    ask_date = datetime(year=int(ask_date[6::]), month=int(ask_date[3:5]), day=int(ask_date[0:2]))
    ask_content = ask_content[1:]

    for i in ask_content:  # Тот же велосипед
        i = i.split('/')
        test_char_code = i[1][-2:-5:-1]
        test_char_code = test_char_code[::-1]
        test_nominal = i[2].split('>')
        test_nominal = test_nominal[-1].split('<')
        test_nominal = int(test_nominal[0])
        test_value = i[4].split('>')
        test_value = test_value[-1].split('<')
        test_value = float(test_value[0].replace(',', '.'))
        if char_code == test_char_code:
            print(f' {test_nominal} ед. {char_code} ровна {test_value} рублям на {ask_date.date()}')


currency_rates('JPY')
currency_rates('USD')
currency_rates('EUR')