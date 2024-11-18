# Человек вводит на сайте номер телефона, 
# ему позволено для удобства использовать кроме плюса 
# и цифр знаки ‘-’, ‘)’, ‘(’ и пробелы. 
# Уберите их из ввода.

with open('Home_Made\\mod3\\Task7\\FileIO\\input.txt', 'r', encoding='utf-8') as f: a = f.read(); f.close();
d = a.replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
w = open('Home_Made\\mod3\\Task7\\FileIO\\output.txt', 'w', encoding='utf-8');  w.write(d); w.close()



