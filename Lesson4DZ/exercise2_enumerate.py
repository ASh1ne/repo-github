def_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [a for i, a in enumerate(def_list[1:]) if def_list[i] < def_list[i+1]]
print(new_list)
