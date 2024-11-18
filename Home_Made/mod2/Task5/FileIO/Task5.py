with open('Home_Made\\mod2\\Task5\\FileIO\\input.txt', 'r', encoding='utf-8') as f:
    a = f.read(34)
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
w = open('Home_Made\\mod2\\Task5\\FileIO\\output.txt', 'w', encoding='utf-8')  # открытие в режиме записи
for domain in reverse:
    print(domain)
    w.write(domain + "\n")  # запись c в файл
w.close()  # закрытие файла

