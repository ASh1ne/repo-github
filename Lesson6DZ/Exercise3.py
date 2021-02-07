"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход).
"""
from functools import reduce


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

    def __str__(self):
        return f'{self.name}, {self.surname}, {self.position}, {self._income}'


class Position(Worker):
    def get_full_name(self):
        return f'Полное имя: {self.name}, {self.surname}'

    def get_total_income(self):
        return reduce(lambda a, x: a+x, self._income.values())


worker1 = Position('Connor', 'McGregor', 'Bouncer', {'wage': 30000, 'bonus': 5000})
worker2 = Position('Michael', 'Jackson', 'Dancer', {'wage': 50000, 'bonus': 15000})
worker3 = Position('Tony', 'Montana', 'Dealer', {'wage': 150000, 'bonus': 20000})

workers = [worker1, worker2, worker3]

for el in workers:
    print(el)
    print(el.get_full_name())
    print(el.get_total_income())
