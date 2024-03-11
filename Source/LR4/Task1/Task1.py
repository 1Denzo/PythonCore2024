# Задача 1.
# На вход подается список чисел через пробел. Напишите функцию выводящую сообщение для списка чисел:
# 1) Все числа равны
# 2) Все числа разные
# 3) Есть равные и неравные числа
with open('input.txt', 'r', encoding='utf-8') as f: a = f.read(); f.close(); n = a.split(" "); ind = []
# a = input("Введите последовательность чисел: ")
for i in range(len(n)):
    if n.count(n[i]) == len(n):
        t = 3; ind.append(t); continue
    if n.count(n[i]) >= 2:
        t = 2; ind.append(t); continue
    else: t = 1; ind.append(t)
match max(ind):
    case 3: print("Все числа одинаковые")
    case 2: print("Есть равные и неравные числа")
    case 1: print('Нет одинаковых чисел')
    case 0: print('Введены некорректные значения')