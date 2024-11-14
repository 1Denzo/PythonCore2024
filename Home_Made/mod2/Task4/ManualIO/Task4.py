# Получение числа от пользователя и проверка его на натуральность
chk = False
while chk == False:
    a = input("Введите натуральное десятичное число : ")
    if int(a) > 0:
        print("Вы ввели число: ", a)
        chk = True
    else: print("Введено неправильное число. Натуральные числа строго больше 0")
def decimal_to_binary(n):
    binary_number = ""
    while n > 0:
        remainder = n % 2  # Остаток от деления на 8
        binary_number = str(remainder) + binary_number  # Добавление остатка к результату
        n = n // 2  # Обновление числа
    
    return binary_number

def decimal_to_octal(n):
    octal_number = ""
    while n > 0:
        remainder = n % 8  # Остаток от деления на 8
        octal_number = str(remainder) + octal_number  # Добавление остатка к результату
        n = n // 8  # Обновление числа
    return octal_number

def decimal_to_hexadecimal(n):
    if n == 0:
        return "0"  # Обработка случая для нуля

    hex_digits = "0123456789ABCDEF"  # Шестнадцатеричные цифры
    hexadecimal_number = ""
    
    while n > 0:
        remainder = n % 16  # Остаток от деления на 16
        hexadecimal_number = hex_digits[remainder] + hexadecimal_number  # Добавление цифры к результату
        n = n // 16  # Обновление числа
    
    return hexadecimal_number

binary = decimal_to_binary(int(a))
octal = decimal_to_octal(int(a))
hex = decimal_to_hexadecimal(int(a))
print("Десятичное натуральное число:", a, ". Двоичное представление числа: ", binary, ". Восьмеричное представление:", octal, ". Шестнадцатиричное представление:", hex)

