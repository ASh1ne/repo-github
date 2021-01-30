from itertools import count
from sys import argv

script_name, start_num, num_step = argv

start_num = int(start_num)
num_step = int(num_step)

for num in count(start_num, num_step):
    if num > 250:
        break
    else:
        print(num)
