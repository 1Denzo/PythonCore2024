with open('input.txt', 'r', encoding='utf-8') as f: a = f.read(20); f.close();
new = sorted(int(n) for n in (a.split(" ", -1))); print(new[1])
w = open('output.txt', 'w', encoding='utf-8'); w.write(str(new[1])); w.close() # открытие, запись, закрытие файла