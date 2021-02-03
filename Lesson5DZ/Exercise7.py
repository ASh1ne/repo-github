"""
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
"""
import json
common_sum = 0
firm_count = 0
firm_list = {}

with open("les5files/lesson7.txt", "r", encoding='UTF-8') as my_file:
    for line in my_file:
        line = line.split()
        bonus = int(line[2]) - int(line[3])
        firm_list[line[0]] = bonus
        if bonus > 0:
            print(f'Прибыль фирмы {line[0]} составляет {bonus:.2f} у.е.')
            common_sum += bonus
            firm_count += 1
        else:
            print(f'Убытки фирмы {line[0]} составляют {-bonus:.2f} у.е.')
    firm_list['average_bonus'] = round((common_sum/firm_count), 2)

with open("les5files/Exercise7_final.json", "a", encoding='UTF-8') as final_file:
    json.dump(firm_list, final_file, ensure_ascii=False)
print(firm_list)
