# 5 Можно ли из слова составить палиндром путем перестановки букв
# (вычеркивать буквы нельзя)? Примеры:
# a - можно
# аа - можно
# ab - нельзя
# aaa - можно
# aab - можно
# aaaabb - можно
# aaaabbc - можно
# aaaabbbc - нельзя
# Видно, что составить можно, если есть не более одной буквы, встречающейся
# нечетное количество раз.

# def polinom_checker(user_input):
#     letter_massiv = [symbol for symbol in user_input]
#     print(letter_massiv)

def check_freq(x):
        freq = {}
        for c in set(x):
            freq[c] = x.count(c)
        return freq

print(check_freq("abbabcbdbabdbdbabababcbcbab"))

# user_input = input("Введите строку: ")
# polinom_checker(user_input)
