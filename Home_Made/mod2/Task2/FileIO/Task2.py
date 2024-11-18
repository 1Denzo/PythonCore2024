with open('Home_Made\\mod2\\Task2\\FileIO\\input.txt', 'r', encoding='utf-8') as f: 
    # Открываем поток чтения из файла input.txt
    a = int(f.read()) # Забираем параметр a из файла input.txt
    f.close() # Закрываем поток чтения из файла
    P = 4 * a # Вычисляем периметр квадрата
    S = a ** 2 # Вычисляем площадь
    D = a * (2 ** (0.5)) # Вычисляем диагональ 
    rounded_D = round(D, 2)
    print("Периметр, Площадь, Диагональ квадрата со строной ", a, " Равны: ", "P =",P,"S =",S,"D =",rounded_D)
    w = open('Home_Made\\mod2\\Task2\\FileIO\\output.txt', 'w', encoding='utf-8')  # открытие в режиме записи
    w.write(str(P)+", " + str(S)+", "+ str(rounded_D))  # запись c в файл
    w.close()  # закрытие файла
