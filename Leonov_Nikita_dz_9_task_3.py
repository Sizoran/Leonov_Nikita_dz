class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(f'Имя: {self.name}, Фамилия: {self.surname}.')

    def get_total_income(self):
        print(f'Доход с учётом премии: {self._income.get("wage") + self._income.get("bonus")}.')

a = Position('Ivan', 'Ivanov', 'Driver', 10000, 3560)
a.get_full_name()
a.get_total_income() 