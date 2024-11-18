# На вход подается доменное имя сайта.
# Необходимо вывести все домены по порядку начиная с домена первого уровня.

with open('Home_Made\\mod3\\Task3\\FileIO\\input.txt', 'r', encoding='utf-8') as f: a = f.read(); f.close(); k = a.split(".", -1)[::-1]; w = open('Home_Made\\mod3\\Task3\\FileIO\\output.txt', 'w', encoding='utf-8')
for n in k: print(n); w.write(n + "\n")
w.close() # открытие, запись, закрытие файла

