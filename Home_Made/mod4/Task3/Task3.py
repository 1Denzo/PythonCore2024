# На вход подается два числа через пробел: a, b.
# Напишите функцию для реализации рекурсивного алгоритма Евклида поиска
# наибольшего общего делителя.

a = input("Введите два числа через запятую: ")
b = a.replace(" ", "").replace(",", " ")
n = []
c = b.split(" ", -1)
num1 = int(c[0])
num2 = int(c[1])


def gcd_recursion(num_1, num_2):
    print(num_1, num_2)
    if num_1 == 0:
        return num_2
    return gcd_recursion(num_2 % num_1, num_1)


gcd = gcd_recursion(num1, num2)
print(gcd)
