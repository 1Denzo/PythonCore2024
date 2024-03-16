# Вводятся числа, пока не встретятся три нуля (не обязательно подряд).
# Вывести их среднее арифметическое.

def input_num():
    counter = 0
    while int(counter) < 3:
        a = input("Введите через пробел три числа: ")
        b = a.split(" ", -1)
        if len(b) != 3: print("Неправильный ввод!"); break
        try:
            c = [int(i) for i in b]
        except ValueError: print("Неправильный ввод!"); break
        for i in range (len(c)):
            if c[i] == 0: counter = counter + 1
        d = (c[0] + c[1] + c[2])//3
        print(d)

input_num()