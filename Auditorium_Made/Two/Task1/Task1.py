# Вводятся три числа - длины отрезков. Можно ли из таких отрезков составить
# треугольник и если можно, то будет ли он равносторонним, равнобедренным или
# прямоугольным?

with open('input.txt', 'r', encoding='utf-8') as f: a = f.read(); f.close()
def trangle_search(a):
    x = (a.split(" ", -1))
    for i in range(len(x)): x[i] = int(x[i])
    x.sort()
    if x[2] < x[0] + x[1]:
        if x[2] == x[0] or x[1] == x[0] or x[2] == x[1]:
            if x[2] == x[0] and x[1] == x[0]: return print("Равносторонний треугольник.")
            else:  print("Равнобедренный треугольник.")
        else: return print("Обычный треугольник.")
    else: print("Треугольник невозможен")
trangle_search(a)