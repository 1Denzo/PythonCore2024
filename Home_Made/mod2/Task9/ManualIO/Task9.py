# Человек вводит на сайте номер телефона, ему позволено для удобства использовать кроме плюса и цифр
#  знаки ‘-’, ‘)’, ‘(’ и пробелы. Уберите их из ввода.
a = input("Введите номер телефона: ")
symbols = []
word = ""
for symbol in a:
    if symbol == ' ' or symbol == '(' or symbol == ')' or symbol == '-':
        symbol = ''
    word = word + symbol
print(word)