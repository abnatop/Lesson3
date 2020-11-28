# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
# деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
# ноль.

def division(digit_one, digit_two):
    if digit_two == 0:
        print('Деление на 0 невозможно.')
        return None
    else:
        return digit_one / digit_two

digit_one = float(input('Введите делимое: '))
digit_two = float(input('Введите делитель: '))

div_result = division(digit_one, digit_two)
print(f'{digit_one} / {digit_two} = {div_result}')