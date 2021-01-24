goods = []
i = 0
exit = ''
print('После окнчания ввода для продолжения обработки ведите "вых" в параметр "название"')
while True:
    goodCard = {'название': '', 'цена': '', 'количество': '', 'ед.': ''}
    num = i+1
    for characteristicName in goodCard.keys():
        paramName = input(f'Введите параметр {characteristicName}: ')
        if paramName == 'вых':
            exit = paramName
            break
        goodCard[characteristicName] = paramName
    if exit:
        break
    goods.append((num, goodCard))
    i += 1
for items in goods:
    print(items)

goodsSort = {}
for count, charact in goods:
    for name, value in charact.items():
        if name in goodsSort:
            goodsSort[name].append(value)
        else:
            goodsSort[name] = [value]
for itemParametr, names in goodsSort.items():
    print(itemParametr, names)
