with open('input.txt', 'r', encoding='utf-8') as f:
    a = f.read(20)
    f.close()   # закрытие файла
    o = b = 0
for simbol in a:
    if simbol == '0':
        b += 1
    if simbol == '1':
        o += 1
w = open('output.txt', 'w', encoding='utf-8')  # открытие в режиме записи
if b == o:
    print("yes")
    w.write("yes")  # запись c в файл
if b != o:
    print("no")
    w.write("no")
w.close()  # закрытие файла






