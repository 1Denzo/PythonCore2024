# На вход подается строка. Напишите функцию для реализации: 
# если из слова можно составить палиндром, то составить его и вывести на экран.

with open('Home_Made\mod4\Task4\input.txt', 'r', encoding='utf-8') as f:
    a = f.read(); f.close()
even = None
symbol = {}  # создание словаря
text1 = "Количесство букв "
if len(a) % 2 == 0:
    print(text1, len(a), " четное.")
    even = True
else: 
    print(text1, len(a), " нечетное.")
    even = False
for x in set(a):
    num = a.count(x)
    symbol[x] = num
    print(x, 'количество в строке', a.count(x))
print(symbol)
marklist = sorted(symbol.items(), key=lambda y: y[1])
sortdict = dict(marklist)

def check_dict_values(d):
    
    # Получаем итератор по значениям и берем первое значение
    value_iterator = iter(d.values())
    first_value = next(value_iterator)
    if even == False:
        # Проверяем, что первое значение равно 1
        if first_value != 1:
            return False

    # Проверяем остальные значения на четность
        for value in value_iterator:
            if value % 2 != 0:  # Проверка на четность
                return False

    elif even == True:
        for value in value_iterator:
            if value % 2 != 0:  # Проверка на четность
                return False
    return True
string_check = check_dict_values(sortdict)
print("Создание полинома возможно: ", string_check)

def build_palindrome(sortdict, even):
    
    left_half = []
    middle_char = ""
    if even:
        for letter, count in sortdict.items():
            # Добавляем половину букв к левой части
            left_half.append(letter * (count // 2))
        # Формируем палиндром
        left_half_str = ''.join(left_half)
        palindrome = left_half_str + left_half_str[::-1]

    else:
        for letter, count in sortdict.items():
            # Добавляем половину букв к левой части
            left_half.append(letter * (count // 2))
            # Если количество букв нечетное, запоминаем эту букву для центра
            if count % 2 != 0:
                middle_char = letter

        # Формируем палиндром
        left_half_str = ''.join(left_half)
        palindrome = left_half_str + middle_char + left_half_str[::-1]

    return palindrome
print("Палиндром: ", build_palindrome(sortdict, even))