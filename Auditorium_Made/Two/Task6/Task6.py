def format_currency(amount):
    if amount % 10 == 1 and amount % 100 != 11:
        return "рубль"
    elif 1 < amount % 10 < 5 and (amount % 100 < 10 or amount % 100 >= 20):
        return "рубля"
    else:
        return "рублей"

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