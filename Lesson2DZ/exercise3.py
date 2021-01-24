timeYear = {'Зима':['1','2','12'],'Весна':['3','4','5'],'Лето':['6','7','8'],'Осень':['9','10','11']}
numMonth = input('Введите номер месяца ')
for season in timeYear.keys():
    for seasonNum in timeYear[season]:
        if numMonth == seasonNum:
            print(f'Время года: {season}')
