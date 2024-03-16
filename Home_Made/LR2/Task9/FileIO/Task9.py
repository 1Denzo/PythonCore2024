with open('input.txt', 'r', encoding='utf-8') as f:
    a = f.read()
    f.close()  # закрытие файла
    symbols = []
    word = ""
for symbol in a:
    if symbol == ' ' or symbol == '(' or symbol == ')' or symbol == '-':
        symbol = ''
    word = word + symbol
print(word)
w = open('output.txt', 'w', encoding='utf-8')  # открытие в режиме записи
w.write(word)  # запись c в файл
w.close()  # закрытие файла





