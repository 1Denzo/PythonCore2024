with open('input.txt', 'r', encoding='utf-8') as f:
    a = int(f.read())
    f.close()
    P = 4 * a
    S = a ** 2
    D = a * (2 ** (0.5))
    rounded_D = round(D, 2)
    print("Периметр, Площадь, Диагональ квадрата со строной ", a, " Равны: ", "P =",P,"S =",S,"D =",rounded_D)
    w = open('output.txt', 'w', encoding='utf-8')  # открытие в режиме записи
    w.write(str(P)+", " + str(S)+", "+ str(rounded_D))  # запись c в файл
    w.close()  # закрытие файла
