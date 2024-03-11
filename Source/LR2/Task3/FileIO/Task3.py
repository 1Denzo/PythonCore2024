with open('input.txt', 'r', encoding='utf-8') as f:
    a = f.read(20)
    f.close()  # закрытие файла
    symbols = []
    digit = ""
    i = 0
for symbol in a:
    i += 1
    if symbol != " ":
        digit = digit + symbol
    if symbol == " " or i == len(a):
        symbols.append(int(digit))
        digit=""
print(symbols)
def sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        if arr[i] <= arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
sort(symbols)
print(symbols)
w = open('output.txt', 'w', encoding='utf-8')  # открытие в режиме записи
w.write(str(symbols[1]))  # запись c в файл
w.close()  # закрытие файла

