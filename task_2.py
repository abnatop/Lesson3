# Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Реализовать вывод данных о
# пользователе одной строкой.

def user_data(name, surname, year_of_birth, live_in_city, email, phone_number):
    result = f'имя: {name}, фамилия: {surname}, год рождения: {year_of_birth}, ' +\
             f'город проживания: {live_in_city}, email: {email}, номер телефона: {phone_number}.'
    return result

print(user_data(
    name='Иван',
    surname='Петров',
    year_of_birth='1980',
    live_in_city='Москва',
    email='ipetrov@gmail.com',
    phone_number='+791663541823'
))