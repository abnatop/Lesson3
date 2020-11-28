# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов.

def my_func(arg_one, arg_two, arg_three):
    ascending_order = [arg_one, arg_two, arg_three]
    ascending_order.sort()
    return ascending_order[1] + ascending_order[2]

print(my_func(10, 5, 1))