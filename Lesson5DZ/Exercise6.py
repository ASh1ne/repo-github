"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
"""
my_file = open("les5files/lesson6.txt", "r", encoding="utf-8")
lessons = my_file.readlines()
new_lessons = {}
for el in lessons:
    el = el.split()
    key = el[0].replace(':', '')
    sum_num = 0
    for number in el[1:len(el)]:
        new_number = (number.replace('(', ' ')).split()
        for element in new_number:
            if element.isdigit():
                sum_num += int(element)
    new_lessons[key] = sum_num
print(new_lessons)
my_file.close()
