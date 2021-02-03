"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

my_file = open("les5files/lesson3.txt", "r", encoding="utf-8")
strings = my_file.readlines()
losers = []
money_count = 0
for string in strings:
    new_string = string.split()
    earn_money = int(new_string[1])
    money_count += earn_money
    if earn_money < 20000:
        losers.append(new_string[0])
print(f'Самые маленькие зарплаты у: {losers}')
print(f'Средняя зарплата: {money_count/len(strings)}')
my_file.close()
