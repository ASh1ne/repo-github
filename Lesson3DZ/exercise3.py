def input_info(count_name):
    digit = int(input(f"Введите {count_name} число: "))
    return digit


def func_sum(a, b, c):
    numbers = [a, b, c]
    numbers = sorted(numbers, reverse=True)
    result = numbers[0]+numbers[1]
    return result


uno = input_info('первое')
dos = input_info('второе')
tres = input_info('третье')

result = func_sum(uno, dos, tres)
print(result)
