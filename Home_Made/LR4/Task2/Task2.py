a = input("Введите два числа через запятую: "); b = a.replace(" ", "").replace(",", " "); n = []; c = b.split(" ", -1)
for i in range(len(c)): n.append(int(c[i]))
r = False; k = int(c[0]); j = int(c[1]); multi = 1
while r == False:
    if  j % 2 == 0 and j != 2: k = k*k; j = j // 2
    if j % 2 == 1 and j != 2: multi = multi * k; j = j - 1
    if j == 1 or j == 2: r = True
print("Множитель равен: " + str(multi) + " Основание: " + str(k) + " Степень: " + str(j))
rez = multi * (k**j)
print("Результат возведения в степень: " + str(rez))