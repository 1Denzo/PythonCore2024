a = input("Введите последовательность символов и, через запятую ключевой символ: ")
b = a[::-1]
key = ''
i = 0
for symbol in b:
        if symbol != ",":
            key = symbol
        if symbol == ",":
            break
print("Ключевой символ для подсчтета " + key)
for let in a:
    if let == key:
        i += 1
    if let != key:
        break
print("В начале строки обнаружено " + str(i) + " ключевых символов.")

