myNumbers = input('введите числа через запятую ').split(',')
print (myNumbers)
count = 0
while count < len(myNumbers)-1:
    myNumbers[count],myNumbers[count+1]=myNumbers[count+1],myNumbers[count]
    count+=2
print(myNumbers)
