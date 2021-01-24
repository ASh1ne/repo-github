userString = input('Введите несколько слов через пробел: ')
for ind, word in enumerate(userString.split(" ")):
    print(ind+1, word[:10], end='\n')
