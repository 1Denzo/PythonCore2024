with open('input.txt', 'r', encoding='utf-8') as f:
    a = f.read(); f.close()
symbol = {}  # создание словаря
for x in set(a):
    num = a.count(x)
    symbol[x] = num
    print(x, 'количество в строке', a.count(x))
print(symbol)
marklist = sorted(symbol.items(), key=lambda y: y[1])
sortdict = dict(marklist)
print(sortdict)
