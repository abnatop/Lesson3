# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии
# Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет
# добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких
# чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого
# завершить программу.

EXIT_CODE = '#'
exit_symbol = ''

result = 0

while exit_symbol != EXIT_CODE:
    digits = input(f'Введите строку чисел, разделенных пробелом (или {EXIT_CODE} для выхода): ')
    if EXIT_CODE in digits:
        digits = digits.replace(EXIT_CODE, '')
        exit_symbol = EXIT_CODE

    digits_list = [float(digit) for digit in digits.split()]
    result += sum(digits_list)
    print(f'Сумма введенных чисел равна {result}.')
