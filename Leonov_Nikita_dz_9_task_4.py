class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановлена')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Скорость авто: {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость превышена! и ровняется: {self.speed} км/ч')
        else:
            print(f'Скорость авто: {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость превышена! и ровняется: {self.speed} км/ч')
        else:
            print(f'Скорость авто: {self.speed} км/ч')


class PoliceCar(Car):
    pass

a = TownCar(70, 'Green', 'Toyota Mark ll', False)
print(a.name, a.speed, a.color, a.is_police)
a.go()
a.turn('налево')
a.show_speed()
a.stop()

d = WorkCar(37, 'Blue', 'Газель Next', False)
print(d.name, d.speed, d.color, d.is_police)
d.go()
d.turn('куда-нибудь')
d.show_speed()
d.stop() 