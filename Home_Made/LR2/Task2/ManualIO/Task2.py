A = input("Введите длинну стороны квадрата A: ")
num_A = int(A)
P = 4 * num_A
S = num_A ** 2
D = num_A * (2 ** (0.5))
rounded_D = round(D, 2)
print("Периметр, Площадь, Диагональ квадрата со строной ", A, " Равны: ", "P =",P,"S =",S,"D =",rounded_D)
