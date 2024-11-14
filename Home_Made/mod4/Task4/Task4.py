# На вход подается строка. Напишите функцию для реализации: 
# если из слова можно составить палиндром, то составить его и вывести на экран.
with open('Home_Made\mod4\Task4\input.txt', 'r', encoding='utf-8') as f:
    a = f.read(); f.close()
even = None
symbol = {}  # создание словаря
if len(a) % 2 == 0:
    print("Количесство букв ", len(a), " четное.")
    even = True
else: 
    print("Количесство букв ", len(a), " нечетное.")
    even = False
for x in set(a):
    num = a.count(x)
    symbol[x] = num
    print(x, 'количество в строке', a.count(x))
print(symbol)
marklist = sorted(symbol.items(), key=lambda y: y[1])
sortdict = dict(marklist)

