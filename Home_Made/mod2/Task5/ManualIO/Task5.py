# На вход подается доменное имя сайта.
# Необходимо вывести все домены по порядку начиная с домена первого уровня.
symbols = []
word = ""
i = 0
a = input("Введите название домена: ")
for symbol in a:
    if symbol == '.':
        symbol = ''
        symbols.append(word)
        word=""
    word = word + symbol
    i += 1
    if i == len(a):
        symbols.append(word)
reverse = symbols[::-1]
for domain in reverse:
    print(domain)


