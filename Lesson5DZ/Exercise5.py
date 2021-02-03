"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint
from functools import reduce
number_string = []
number_count = int(input('Введите количество чисел: '))
i = 0
while i < number_count:
    a = str(randint(1, 30))
    number_string.append(a)
    i += 1
number_string = ' '.join(number_string)
with open("les5files/lesson5.txt", "w") as my_file:
    my_file.write(number_string)

my_file = open("les5files/lesson5.txt", "r")
file_string = [int(x) for x in (my_file.read().split())]
sum_all = reduce(lambda sum_num, x: sum_num + int(x), file_string)
print(sum_all)
my_file.close()
