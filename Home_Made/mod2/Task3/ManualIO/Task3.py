
symbols = []
checker = False
for i in range(3):
    checker = False
    while checker != True:
        a = input("Введите " + str(i) + " число a массива: ")
        if int(a) <= -1000 and int(a) <= 1000:
            symbols.append(int(a))
            checker = True
        else: 
            print("Число находится вне диапазона от -1000 до 1000 или введен неверный символ!")
print(symbols)
def sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        if arr[i] <= arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
if symbols[0] > symbols[1]:
    sort(symbols)
print(symbols[1])

