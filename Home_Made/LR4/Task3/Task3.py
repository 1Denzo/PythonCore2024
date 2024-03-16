a = input("Введите два числа через запятую: "); b = a.replace(" ", "").replace(",", " "); n = []; c = b.split(" ", -1)
num1 = int(c[0]); num2 = int(c[1])
def gcd_recursion(num1, num2):
    print(num1, num2)
    if num1 == 0:
        return num2
    return gcd_recursion(num2 % num1, num1)
gcd = gcd_recursion(num1, num2); print(gcd)