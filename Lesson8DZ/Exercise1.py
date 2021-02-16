"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
"""


class Date:
    def __init__(self, input_date):
        self.date = input_date

    @classmethod
    def convert_date(cls, date):
        int_date = []
        for el in date.split('-'):
            int_date.append(int(el))
        return int_date

    @staticmethod
    def validate_date(date):
        if int(date.split('-')[1]) in [1, 3, 5, 7, 8, 10, 12] and int(date.split('-')[0]) in range(0, 32):
            return 'Данные верны, 31 день'
        elif int(date.split('-')[1]) == 2:
            if int(date.split('-')[2]) in range(0, 2200, 4) and int(date.split('-')[0]) in range(0, 30):
                return 'Данные верны. Февраль високосный'
            elif int(date.split('-')[0]) in range(0, 29):
                return 'Данные верны. Февраль невисокосный'
            else:
                return 'Ошибка ввода'
        elif int(date.split('-')[1]) in [4, 6, 9, 11] and int(date.split('-')[0]) in range(0, 31):
            return 'Данные верны, 30 дней'
        else:
            return 'Ошибка ввода. Проверьте данные'


inp_date = input('Введите дату в формате ДД-ММ-ГГГГ: ')
print(Date.convert_date(inp_date))
print(Date.validate_date(inp_date))
