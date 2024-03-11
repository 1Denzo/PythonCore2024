with open('input.txt', 'r', encoding='utf-8') as f: a = f.read(); f.close(); w = open('output.txt', 'w', encoding='utf-8'); t = False; n = a.split(" ");
for i in range(len(n)): t = True if n.count(n[i]) >= 2 else False
w.write(str(t)); w.close()







