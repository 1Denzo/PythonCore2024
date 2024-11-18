with open('Home_Made\\mod2\\Task1\\FileIO\\input.txt', 'r', encoding='utf-8') as f:
    a = int(f.read(3))
    b = int(f.read(4).replace(', ', ''))
    f.close()
    c = a % b
    print(c)
    w = open('output.txt', 'w', encoding='utf-8')  # открытие в режиме записи
    w.write(str(c))  # запись c в файл
    w.close()  # закрытие файла
