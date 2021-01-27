def input_number(number_name):
    digit = int(input(f"Введите {number_name}: "))
    return digit


def division(a, b):
    try:
        result = (a / b)
        return result
    except ZeroDivisionError:
        print('На ноль делить нельзя')


a = input_number('Делимое')
b = input_number('Делитель')
print(division(a, b))
