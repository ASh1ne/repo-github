"""
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
my_file = open("les5files/lesson4.txt", "r", encoding="utf-8")
rus_numbers = ['Один', 'Два', 'Три', 'Четыре']
count = 0
for string in my_file:
    new_string = string.split()
    new_string[0] = rus_numbers[count]
    new_string = ' '.join(new_string)
    with open("les5files/lesson4new.txt", "a") as my_new_file:
        my_new_file.write(new_string+'\n')
    count += 1
my_file.close()
