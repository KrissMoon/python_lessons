# Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой

def user(name, surname, birth, town, email, phone):
    print(f'{name}, {surname}, {birth}, {town}, {email}, {phone} ')


name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
birth = int(input('Введите ваш год рождения: '))
town = input('Введите ваш город проживания: ')
email = input('Введите ваш email: ')
phone = int(input('Введите ваш телефон: '))
user(name=name, surname=surname, birth=birth, town=town, email=email, phone=phone)


