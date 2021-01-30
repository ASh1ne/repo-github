from itertools import cycle
from sys import argv

script_name, iter_count = argv
i = 0
words = ['Houston', 'we', 'have', 'a', 'trouble']

iter_count = int(iter_count)
for word in cycle(words):
    if i > iter_count:
        break
    print(word)
    i += 1
