a = input("Введите последовательность 0 и 1: ")
k = b = 0
for simbol in a:
    if simbol == '0':
        b += 1
    if simbol == '1':
        k += 1
if b == k:
    print("yes")
if b != k:
    print("no")


