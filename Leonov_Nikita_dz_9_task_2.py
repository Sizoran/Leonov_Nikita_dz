class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass_asphalt(self):
        my_result = (self.__length * self.__width * 25 * 5) / 1000
        print(f'При ширине дороги {self.__width}м, длинне дороги {self.__length}м, '
              f'толщиной дорожного покрытия в 5см и удельном весе в 25кг на 1м.кв с толщиной в 1см покрытия асфальтом. '
              f'Общая масса асфальта равна: {my_result} тонн.')


my_road = Road(5000, 20)
my_road.mass_asphalt() 