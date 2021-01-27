def input_numbers():
    number_sum = 0
    numbers = (input('Введите числа через пробел: ').split(' '))
    for str_a in numbers:
        if str_a == 'exit':
            global flag
            flag = True
            break
        else:
            int_a = int(str_a)
            number_sum += int_a
    return number_sum


print('Для выхода наберите "exit"')
flag = ''
sum_numbers = 0

while True:
    sum_numbers += input_numbers()
    print(sum_numbers)
    if flag:
        break