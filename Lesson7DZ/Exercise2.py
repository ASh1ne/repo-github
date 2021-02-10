"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
"""
from functools import reduce


def textile_sum(cloth_list):
    return reduce(lambda temp, x: temp + x.textile, cloth_list, 0)


class Clothes:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return self.name


class Coat(Clothes):

    @property
    def textile(self):
        return round((self.size/6.5 + 0.5), 2)


class Suit(Clothes):

    @property
    def textile(self):
        return round((2 * self.size + 0.3), 2)


coat1 = Coat('Пальто', 34)
suit1 = Suit('Костюм', 1.8)
coat2 = Coat('ДругаяМодельпальто', 30)
suit2 = Suit('ДругойКостюм', 1.65)
coat3 = Coat('ЕщёКлассноеПальто', 28)

clothes_list = [
    coat1,
    coat2,
    suit1,
    suit2,
    coat3
]

for obj in clothes_list:
    print(f'На предмет одежды "{obj.name}" необходимо {obj.textile}м материала')

common_textile = textile_sum(clothes_list)
print(f'Общее количество материала на партию: {common_textile}м')
