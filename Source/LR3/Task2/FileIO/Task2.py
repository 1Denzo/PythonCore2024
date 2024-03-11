with open('input.txt', 'r', encoding='utf-8') as f: a = f.read(20); f.close();
d = int(a); b = str(bin(d)[2:]); e = str(oct(d)[2:]); r = str(hex(d)[2:]); print(b + " " + e + " " + r)
w = open('output.txt', 'w', encoding='utf-8'); w.write(str(new[1])); w.close() # открытие, запись, закрытие файла

