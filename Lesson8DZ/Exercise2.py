class MyZeroError(Exception):
    def __init__(self, text):
        self.txt = text

       
a, b = input('a: '),input('b: ')
try:
    if int(b) == 0:
       raise MyZeroError('Смотри что вводишь! На ноль делить нельзя!')
    result = int(a) / int(b)
except ValueError:
    print('Проверь тип вводных данных')
except MyZeroError as mze:
    print(mze)
else:
    print(result)