"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
"""


def enter_matrix(number):
    i = 1
    matrix = []
    while True:
        new_string = input(f'Введите {i} строку матрицы {number}: ')
        if i == 1:
            len_matrix = len(new_string.split())
        if new_string == '':
            break
        if not new_string.replace(' ', '').isdigit():
            print(f'Неверный символ')
            continue
        if len(new_string.split()) != len_matrix:
            print('Неверная длина строки! Повторите ввод')
            continue
        matrix.append(new_string)
        i += 1
    return matrix


class Matrix:
    def __init__(self, true_matrix):
        self.true_matrix = true_matrix

    def __str__(self):
        return '\n'.join(self.true_matrix)

    def __add__(self, other):
        new_true_matrix = []
        for el1, el2 in zip(self.true_matrix, other.true_matrix):
            c = [int(x) + int(y) for x, y in zip(el1.split(), el2.split())]
            new_true_matrix.append(c)
        return new_true_matrix


print(
    'Вводите поочередно строки матрицы.\nВводите числа через пробел\nПосле окончания ввода строки нажмите ENTER.\n'
    'Длины строк должны быть одинаковыми.\nДля окончания ввода оставьте строку пустой: ')

matrix1 = enter_matrix('1')
matrix2 = enter_matrix('2')

m1 = Matrix(matrix1)
m2 = Matrix(matrix2)

print(m1)
print(m2)

if len(m1.true_matrix) != len(m2.true_matrix) or len(m1.true_matrix[0].split()) != len(m2.true_matrix[0].split()):
    print('Матрицы нельзя сложить!')
else:
    c = m1 + m2
    for el in c:
        print(el)
