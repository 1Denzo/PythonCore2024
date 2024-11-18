# Для введенного в десятичном коде натурального числа найти представление
# в двоичном, восьмеричном и шестнадцатеричном кодах. 
# Если введено не натуральное число, вывести диагностику: «Неверный ввод»

with open('Home_Made\\mod3\\Task2\\FileIO\\input.txt', 'r', encoding='utf-8') as f: a = f.read(20); f.close()
if a > 0: d = int(a); b = str(bin(d)[2:]); e = str(oct(d)[2:]); r = str(hex(d)[2:]); res = str(b + " " + e + " " + r);print(res);w = open('Home_Made\\mod3\\Task2\\FileIO\\output.txt', 'w', encoding='utf-8'); w.write(res); w.close() # открытие, запись, закрытие файла
else: print("Неверный ввод!")
