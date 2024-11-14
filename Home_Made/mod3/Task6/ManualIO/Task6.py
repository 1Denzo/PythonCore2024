a = input("Введите последовательность чисел: "); t = False; n = a.split(" ");
for i in range(len(n)): t = True if n.count(n[i]) >= 2 else False
print(str(t))

