timeYear = [1,2,3,4,5,6,7,8,9,10,11,12]
nuMon = int(input('Введите месяц '))

if nuMon in timeYear[3:5]:
    print("Spring")
elif nuMon in timeYear[6:8]:
    print("Summer")
elif nuMon in timeYear[9:11]:
    print("Autumn")
else:
    print("Winter")
