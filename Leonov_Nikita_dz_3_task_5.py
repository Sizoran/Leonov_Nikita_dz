from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count_jokes, repeat='on'):
    count_jokes = int(count_jokes)
    if repeat == 'on':
        while count_jokes > 0:
            count_jokes -= 1
            print(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    else:
        try:
            while count_jokes > 0:
                count_jokes -= 1
                word_1 = choice(nouns)
                word_2 = choice(adverbs)
                word_3 = choice(adjectives)
                print(f'{word_1} {word_2} {word_3}')
                nouns.remove(word_1)
                adverbs.remove(word_2)
                adjectives.remove(word_3)
        except IndexError:
            print('Шутки кончились :(')


user_input = input("Введите число шуток: ")
user_repeat = input('Ходите что бы слова в шутках повторядись? (on/off): ')
get_jokes(user_input, user_repeat)