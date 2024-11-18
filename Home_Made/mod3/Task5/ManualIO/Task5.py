# Дан список слов. Составить из последних букв каждого слова новое.

a = input("Введите несколько слов через пробел: "); word, new_word = "", ""; k = a.split(" ", -1)
for i in range(len(k)): word = k[i]; new_word += word[-1]
print(new_word)


