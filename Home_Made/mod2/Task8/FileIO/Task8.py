with open('Home_Made\lr2\Task8\FileIO\input.txt', 'r', encoding='utf-8') as f:
    a = f.read()
    f.close()  # закрытие файла
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
print(symbols)
print(new_word)
w = open('Home_Made\lr2\Task8\FileIO\input.txt', 'w', encoding='utf-8')  # открытие в режиме записи
w.write(new_word)  # запись c в файл
w.close()  # закрытие файла





