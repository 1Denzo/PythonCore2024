# На вход подается строка s и символ i.
# Необходимо найти количество символов i, расположенных в начале строки.
with open('Home_Made\lr2\Task7\FileIO\input.txt', 'r', encoding='utf-8') as f:
    a = f.read(20)
    f.close() # закрытие файла
b = a[::-1]
key = ''
i = 0
for symbol in b:
        if symbol != ",":
            key = symbol
        if symbol == ",":
            break
print(key)
for let in a:
    if let == key:
        i += 1
    if let != key:
        break
print(i)
w = open('Home_Made\lr2\Task7\FileIO\output.txt', 'w', encoding='utf-8')  # открытие в режиме записи
w.write(str(i))  # запись c в файл
w.close()  # закрытие файла





