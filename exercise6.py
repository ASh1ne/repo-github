dayCount = 0
print("Введите начальную дистанцию")
defaultDistance = int(input())
print("Введите необходимый результат")
upgradeDistance = int(input())

while defaultDistance <= upgradeDistance:
    defaultDistance = defaultDistance + (defaultDistance*0.1)
    dayCount += 1

print(f"Спортсмен достиг результата {defaultDistance:.2f} на {dayCount} день")