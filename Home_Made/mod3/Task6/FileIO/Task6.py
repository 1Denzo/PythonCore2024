# На вход подается последовательность целых чисел. 
# Требуется определить, присутствуют ли в этой последовательности одинаковые числа.
# Результат вернуть в формате Boolean.

with open('Home_Made\\mod3\\Task6\\FileIO\\input.txt', 'r', encoding='utf-8') as f: a = f.read(); f.close(); w = open('Home_Made\\mod3\\Task6\\FileIO\\output.txt', 'w', encoding='utf-8'); t = False; n = a.split(" ");
for i in range(len(n)): t = True if n.count(n[i]) >= 2 else False
w.write(str(t)); w.close()







