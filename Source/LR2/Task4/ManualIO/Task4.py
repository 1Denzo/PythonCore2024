
symbols = []
for i in range(3):
    a = input("Введите " + str(i) + " число a массива: ")
    symbols.append(int(a))
print(symbols)
def sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        if arr[i] <= arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
if symbols[0] > symbols[1]:
    sort(symbols)
print(symbols)

