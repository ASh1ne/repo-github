from functools import reduce
new_list = [a for a in range(99, 1001) if a % 2 == 0]
generate = reduce(lambda a, x: a * x, new_list)
print(generate)
