class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} рисует')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} рисует')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} рисует')


a = Pen('ручка')
a.draw()

b = Pencil('карандаш')
b.draw()

s = Handle('маркер')
s.draw() 