"""
 Реализовать программу работы с органическими клетками.
"""


class SmallCell(Exception):
    def __init__(self, text):
        self.txt = text


class Cell:
    def __init__(self, name, cell_number):
        self.name = name
        self.cell_number = cell_number

    def __str__(self):
        return f'Клетка {self.name} состоит из {self.cell_number} ячеек'

    def __add__(self, other):
        return self.cell_number + other.cell_number

    def __sub__(self, other):
        try:
            result = self.cell_number - other.cell_number
            if result < 0:
                raise SmallCell('Вы не можете уменьшить клетку!')
        except SmallCell as sc:
            return 'Вы не можете уменьшить клетку!'
        else:
            return result

    def __mul__(self, other):
        return self.cell_number * other.cell_number

    def __truediv__(self, other):
        try:
            return self.cell_number // other.cell_number
        except ZeroDivisionError:
            return 'Нет возможности разделить клетки'

    def make_order(self):
        sign = '*'
        cell_string = sign * self.cell_number
        cell_string = '\n'.join(cell_string[i:i+5] for i in range(0, len(cell_string)-1, 5))
        return cell_string


c1 = Cell('Cell1', 19)
c2 = Cell('Cell2', 9)

print(c1+c2)
print(c1-c2)
print(c1*c2)
print(c1/c2)
print(c1.make_order())
