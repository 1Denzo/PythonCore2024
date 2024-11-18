# Рассмотрим три числа a, b и c. Упорядочим их по возрастанию.
# Какое число будет стоять между двумя другими?

with open('Home_Made\\mod3\\Task1\\FileIO\\input.txt', 'r', encoding='utf-8') as f: a = f.read(20); f.close();
new = sorted(int(n) for n in (a.split(" ", -1))); print(new[1])
w = open('Home_Made\\mod3\\Task1\\FileIO\\output.txt', 'w', encoding='utf-8'); w.write(str(new[1])); w.close() # открытие, запись, закрытие файла