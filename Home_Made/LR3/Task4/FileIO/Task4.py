with open('input.txt', 'r', encoding='utf-8') as f: a = f.read(); f.close(); w = open('output.txt', 'w', encoding='utf-8')
if a.count('1') != a.count('0'): w.write("no");  w.close()
if a.count('1') == a.count('0'): w.write("yes");  w.close()







