with open('input.txt', 'r', encoding='utf-8') as f:
    a = f.read(20)
    f.close()  # закрытие файла
    symbols = []
    word = ""
    i = 0
for symbol in a:
    if symbol == '.':
        symbol = ''
        symbols.append(word)
        word=""
    word = word + symbol
    i += 1
    if i == len(a):
        symbols.append(word)
reverse = symbols[::-1]
w = open('output.txt', 'w', encoding='utf-8')  # открытие в режиме записи
for domain in reverse:
    print(domain)
    w.write(domain + "\n")  # запись c в файл
w.close()  # закрытие файла

