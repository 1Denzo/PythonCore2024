with open('input.txt', 'r', encoding='utf-8') as f: a = f.read(); f.close(); k = a.split(".", -1)[::-1]; w = open('output.txt', 'w', encoding='utf-8')
for n in k: print(n); w.write(n + "\n")
w.close() # открытие, запись, закрытие файла

