def re_word(word):
    new_word = ''
    i = 0
    for a in word:
        if i == 0:
            new_a = a.upper()
            new_word += new_a
            i += 1
        else:
            new_word += a
    return(new_word)


new_words = ''
default_words = input('Введите строку через пробел: ')
default_words = default_words.split()
for word in default_words:
    new_words += (re_word(word)+' ')
print(new_words)
