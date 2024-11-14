with open('Home_Made\lr2\Task4\FileIO\input.txt', 'r', encoding='utf-8') as f:
    a = f.read(20)
    f.close()  # закрытие файла
d = int(a)
# while d > 0:
#     b = str(d % 2) + b
#     d = d // 2
b = str(bin(d)[2:])
e = str(oct(d)[2:])
rez = str(hex(d)[2:])
print(b + " " + e + " " + rez)
w = open('Home_Made\lr2\Task4\FileIO\output.txt', 'w', encoding='utf-8')  # открытие в режиме записи
w.write(b + ", " + e + ", " + rez)  # запись c в файл
w.close()  # закрытие файла

