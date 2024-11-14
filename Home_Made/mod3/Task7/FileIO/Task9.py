with open('input.txt', 'r', encoding='utf-8') as f: a = f.read(); f.close();
d = a.replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
w = open('output.txt', 'w', encoding='utf-8');  w.write(d); w.close()

# s[0] = a; num = (s[i].replace(k[i], "") for i in range (len(k))); print(s[1])
# b = (a.replace(k[i], "") for i in k); print(b)





