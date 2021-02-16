class MyInputError(Exception):
    pass

new_list = []

while True:
    new_el = input('Введите число: ')
    if new_el == 'stop':
        break
    try:
        if not new_el.isdigit():
            raise MyInputError('Введены не цифры!')
    except MyInputError:
        print('Неверные данные. Повторите ввод')
    else:
        new_list.append(new_el)

print(new_list)