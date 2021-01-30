def fact():
    a = 1
    num_fact = 1
    while a <= fact_count:
        num_fact *= a
        yield num_fact
        a += 1


fact_count = int(input('Введите число: '))
for el in fact():
    print(el)
print(fact())
