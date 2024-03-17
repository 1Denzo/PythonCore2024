# Правильно просклонять слово "лет" в зависимости от введеного числительного.
def format_currency(amount):
    if amount == 1:
        return "год"
    elif 1 < amount < 5 :
        return "года"
    else:
        return "лет"

def main():
    chk = False
    while chk == False:
        number = input("Введите число: ")
        if number.isdigit(): chk = True
        else: print("Неправильный ввод, пожалуйста повторите.")
    number = int(number)
    result = format_currency(number)
    print(f"{number} {result}")

main()