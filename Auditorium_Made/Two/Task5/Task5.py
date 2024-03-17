def check_palindrome_possible(s):
    # Подсчитаем количество символов
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Подсчитаем количество символов с нечетным количеством встреч
    odd_chars = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_chars += 1

    # Если длина строки четная, все символы должны встречаться четное количество раз,
    # иначе может быть только один символ с нечетным количеством встреч
    if len(s) % 2 == 0 and odd_chars == 0:
        return True
    elif len(s) % 2 != 0 and odd_chars == 1:
        return True
    else:
        return False


# Пример использования
s = "aaabbccggddssddaffcccczzz"
if check_palindrome_possible(s):
    print("Из символов строки можно составить палиндром")
else:
    print("Из символов строки невозможно составить палиндром")