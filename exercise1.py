a = 10
sayHi = "Hello, World"
print(sayHi+" "+str(a))
print(a)
print("Ели ли вы овощи сегодня")
answer = input()
if(answer == 'да'):
    print("Сколько овощей?")
    times = int(input())
    print(f"Товарищ ел овощи в количестве {times} шт.")
else:
    print("Очень плохо. Ешьте овощи")