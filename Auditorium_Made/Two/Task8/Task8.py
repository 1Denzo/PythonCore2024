# 8 На вход подается число, формы склонения слова (для 1,2,5).
#   Написать программу, выводящую существительное в правильной форме для любого введенного числа.
def format_word(in_mas, amount):
    if amount == 1:
        return in_mas[0]
    elif 1 < amount < 5 :
        return in_mas[1]
    else:
        return in_mas[2]

def input_checker():
    chk = 0
    while chk < 4:
        in_str = input(
            "Введите строку с формами склонения слова (для 1,2,5) и необходиммым для вывода числом (пластилин, пластилина, пластилинов, 5): ")
        in_mas = in_str.replace(",", "").split(" ", -1)
        for i in range(len(in_mas)):
            if i == len(in_mas) - 1 and in_mas[i].isdigit(): chk += chk; return in_mas
            if in_mas[i].isalpha(): chk += chk
            else:
                print("Неправильный ввод, пожалуйста повторите."); break

def main():
    in_mas = input_checker()
    amount = int(in_mas[-1])
    result = format_word(in_mas, amount)
    print(f"{amount} {result}")

main()