# Возводить в степень можно гораздо быстрее, чем за n умножений!
# Для этого нужно воспользоваться следующими рекуррентными соотношениями:
# a^n = (a^2)^n/2  при четном n,
# a^n = a × a^n−1 при нечетном n.
# На вход подается два числа через пробел: a, n. Напишите функцию для реализации алгоритма быстрого возведения в степень с помощью рекурсивной функции.

a = input("Введите два числа через запятую - число и степень с которую возводим: "); b = a.replace(" ", "").replace(",", " "); n = []; c = b.split(" ", -1)
for i in range(len(c)): n.append(int(c[i]))
r = False; k = int(c[0]); j = int(c[1]); multi = 1
while r == False:
    if  j % 2 == 0 and j != 2: k = k*k; j = j // 2
    if j % 2 == 1 and j != 2: multi = multi * k; j = j - 1
    if j == 1 or j == 2: r = True
print("Множитель равен: " + str(multi) + " Основание: " + str(k) + " Степень: " + str(j))
rez = multi * (k**j)
print("Результат возведения в степень: " + str(rez))