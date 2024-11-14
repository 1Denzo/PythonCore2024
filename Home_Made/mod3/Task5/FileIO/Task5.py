with open('input.txt', 'r', encoding='utf-8') as f: a = f.read(); f.close(); word, new_word = "", ""; k = a.split(" ", -1)
for i in range(len(k)): word = k[i]; new_word += word[-1]
w = open('output.txt', 'w', encoding='utf-8'); w.write(new_word); w.close()





