# Является ли введенная строка палиндромом?
# (читается одинаково слева направо и справа налево)
def polinom_checker(user_input):
    user_reverse = user_input[::-1]
    if user_reverse != user_input:
        print("Строка не является полиномом.")
    else:
        print("Строка является полиномом.")


user_input = input("Введите строку: ")
polinom_checker(user_input)
