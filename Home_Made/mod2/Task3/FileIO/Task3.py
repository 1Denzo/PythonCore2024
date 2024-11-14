with open('Home_Made\\lr2\\Task3\\FileIO\\input.txt', 'r', encoding='utf-8') as f:
    a = f.read(20)
    f.close()  # закрытие файла
symbols = []
digit = ""
i = 0
print (len(a))
for symbol in a:
    if symbol != " ":
        digit = digit + symbol
    else: 
        if symbol == " " or i == len(a):
                if int(digit) >= -1000 and int(digit) <= 1000:
                    symbols.append(int(digit))
                    digit=""
                else: 
                    print("Число находится вне диапазона от -1000 до 1000 или введен неверный символ!")
                    digit=""
    i += 1
def sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        if arr[i] <= arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
if   len(symbols) < 3:
    print("Массив не считан.")
else: 
    sort(symbols)
    print(symbols)
    w = open('Home_Made\\lr2\\Task3\\FileIO\\output.txt', 'w', encoding='utf-8')
    w.write(str(symbols[1]))  # запись c в файл
    w.close()  # закрытие файла
