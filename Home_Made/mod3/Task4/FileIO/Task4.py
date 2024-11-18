# Строка состоит из 0 и 1. Выведите ‘yes’,
# если количество единиц совпадает с количеством нулей. 
# И ‘no’ в противном случае.

with open('Home_Made\\mod3\\Task4\\FileIO\\input.txt', 'r', encoding='utf-8') as f: a = f.read(); f.close(); w = open('Home_Made\\mod3\\Task4\\FileIO\\output.txt', 'w', encoding='utf-8')
if a.count('1') != a.count('0'): w.write("no");  w.close()
if a.count('1') == a.count('0'): w.write("yes");  w.close()







