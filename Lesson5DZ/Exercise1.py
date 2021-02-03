"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
 Об окончании ввода данных свидетельствует пустая строка.
"""

my_txt = open(r'les5files/lesson1.txt', 'w')
new_string = []
while True:
    input_string = input('Введите строку. Для окончания ввода оставьте строку пустой: ')
    if input_string == '':
        break
    new_string.append(input_string+'\n')
my_txt.writelines(new_string)
my_txt.close()
