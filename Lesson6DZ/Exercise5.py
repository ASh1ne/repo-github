"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.
"""


class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Начало отрисовки объекта: Ручка')


class Pencil(Stationery):
    def draw(self):
        print(f'Начало отрисовки объекта: Карандаш')


class Handle(Stationery):
    def draw(self):
        print(f'Начало отрисовки объекта: Маркер')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

all_stationery = [pen, pencil, handle]
for el in all_stationery:
    print(el)
    el.draw()
