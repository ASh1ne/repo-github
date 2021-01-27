def num_degree(number, degree):
    if degree == 1:
        return number
    elif degree < 0:
        return 1 / (number*num_degree(number, -degree-1))
    else:
        return number*num_degree(number, degree-1)


number = int(input('Введите число: '))
while True:
    degree = int(input('Введите отрицательную степень числа: '))
    if degree <= 0:
        break

print(num_degree(number, degree))
