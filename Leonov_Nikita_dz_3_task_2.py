dictionary = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}


def num_translate_adv(key):
    """ Numeral translator with string checking """
    if key == key.lower():
        print(dictionary.get(key))
    elif key == key.capitalize():
        print((dictionary.get((key.lower()))).capitalize())
    else:
        return None


user_ask = input("input num in string plz: ")
num_translate_adv(user_ask)