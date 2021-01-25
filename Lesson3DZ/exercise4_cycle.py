def num_degree(number, degree):
    count = 0
    result = 1
    while count > degree:
        result = result/number
        count -= 1
    return result


digit = int(input('Введите число для возведения в степень: '))
while True:
    dig_degree = int(input('Введите целое отрицательное число: '))
    if dig_degree < 0:
        break
res = num_degree(digit, dig_degree)
print(res)
