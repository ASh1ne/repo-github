rate = [8,7,7,6,3,3,]
while True:
    newDigit = (input('Введите новое значение рейтинга\nЧтобы выйти введите "x":  '))
    if newDigit == 'x':
        break
    newDigit = int(newDigit)
    if newDigit in rate:
       rate.insert(rate.index(newDigit)+rate.count(newDigit), newDigit)
    else: 
        rate.append(newDigit)
        rate.sort(reverse=True)
    print(rate)
