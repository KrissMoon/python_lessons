# Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    args = [arg_1, arg_2, arg_3]
    minimal = min(args)
    args.pop(args.index(minimal))
    return sum(args)


arg_1 = int(input('Введите arg_1: '))
arg_2 = int(input('Введите arg_2: '))
arg_3 = int(input('Введите arg_3: '))
print(my_func(arg_1, arg_2, arg_3))