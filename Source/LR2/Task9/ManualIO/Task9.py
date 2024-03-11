a = input("Введите несколько слов через пробел: ")
symbols = []
word = ""
new_word = ""
i = 0
for symbol in a:
    if symbol == ' ':
        symbol = ''
        symbols.append(word)
        new_word += word[-1]
        word=""
    word = word + symbol
    i += 1
    if i == len(a):
        symbols.append(word)
        new_word += word[-1]
print("Новое слово составленное из последних букв слов введенной последовательности " + new_word)

