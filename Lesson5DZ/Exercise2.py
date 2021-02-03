"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

word_count = 0
my_file = open("les5files/lesson2.txt", "r", encoding="utf-8")
strings = my_file.readlines()
string_count = len(strings)
for index, string in enumerate(strings):
    count = len(string.split())
    print(f'В строке {index+1} слова в количестве {count} шт.')
    word_count += count
print(f'В файле {string_count} строк и слова в количестве {word_count} шт.')
my_file.close()
