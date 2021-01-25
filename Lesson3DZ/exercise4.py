def num_degree(num, deg):
    res = num ** deg
    return res


num = int(input('Введите число для возведения в степень: '))
while True:
    deg = int(input('Введите целое отрицательное число: '))
    if deg < 0:
        break

print(num_degree(num, deg))
