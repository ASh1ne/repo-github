"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Вычислить массу необходимого асфальта.
"""


class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass_calc(self, thickness):
        return (self.__length * self.__width * 25 * thickness)/1000


def input_param(name, units):
    return int(input(F'Введите {name} в {units}: '))


while True:
    new_len = input_param('длину', 'метрах')
    new_width = input_param('ширину', 'метрах')
    new_thick = input_param('толщину слоя', 'сантиметрах')
    if new_len > 0 and new_width > 0 and new_thick > 0:
        break
    else:
        print('Проверьте правильность введенных данных!')

new_road = Road(new_len, new_width)
print(f'Масса асфальта: {new_road.mass_calc(new_thick)}')
