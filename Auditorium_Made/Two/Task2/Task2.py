# Вводятся числа, пока не встретится ноль. Вывести их среднее арифметическое.

checker = False
while checker == False:
    a = input("Введите через пробел два числа: ")
    b = a.split(" ", -1)
    if b[0].isdigit() and b[1].isdigit():
        c = (int(b[0]), int(b[1]))
        d = (c[0] + c[1])//2
        print(d)
        if c[0] == 0 or c[1] == 0: checker = True
        continue
    print("Неправильный ввод!")